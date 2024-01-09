import json
from pathlib import Path
from jsonpath import jsonpath
from collections import OrderedDict
from copy import deepcopy
from vic_utilities.vic_log import get_logger


class VicJson(dict):
    _all_items = None
    need_update = True
    logger = get_logger(Path(__file__).name)

    def __init__(self, json_object, logger=None):
        if isinstance(json_object, str):
            self.json_object = json.loads(json_object)
        elif isinstance(json_object, dict):
            self.json_object = json_object
        else:
            raise ValueError("please provide a json object or json string")
        if logger:
            self.logger = logger
        super().__init__(self.json_object)

    def __str__(self):
        return json.dumps(self.json_object, indent=2)

    @staticmethod
    def ipath_to_path(ipath):
        path = "$"
        if not isinstance(ipath, list):
            raise ValueError("ipath should be a list")
        for _ in ipath:
            if not isinstance(_, str) and not isinstance(_, int):
                raise ValueError("Invalid ipath format")
            path = "{}[{}]".format(path, _)
        return path

    @staticmethod
    def path_to_ipath(path):
        def split_list(_list, sep):
            new_list = list()
            for _ in _list:
                if not '' == _:
                    new_list.extend(_.split(sep))
            return new_list

        ipath = path[1:].replace("'", "").replace('"', '').split("[")
        ipath = split_list(ipath, "]")
        ipath = split_list(ipath, ".")
        return [_ for _ in ipath if _ != '']

    @staticmethod
    def static_add_value_of_ipath(json_object, ipath, value, ignore_error=True, logger=None):
        return VicJson.static_update_value_of_ipath(json_object, ipath, value, ignore_error=ignore_error, logger=logger, allow_create_path=True)

    @staticmethod
    def static_add_value_of_path(json_object, path, value, ignore_error=True, logger=None):
        return VicJson.static_update_value_of_path(json_object, path, value, ignore_error=ignore_error, logger=logger, allow_create_path=True)

    @staticmethod
    def static_update_value_of_ipath(json_object, ipath, value, track=None, ignore_error=True, _copy=True, logger=None, allow_create_path=False):
        if logger:
            _logger = logger
        else:
            _logger = VicJson.logger
        is_first = False
        if not track:
            track = list()
            is_first = True
        if _copy:
            json_object = deepcopy(json_object)
        try:
            k = ipath.pop(0)
            track.append(k)
            if isinstance(json_object, list):
                k = int(k)
                if allow_create_path and k <= len(json_object):
                    json_object = json_object[:k] + [{}] + json_object[k:]
            else:
                if allow_create_path and json_object.get(k) is None:
                    json_object[k] = dict()
            if len(ipath) > 0:
                json_object[k] = VicJson.static_update_value_of_ipath(json_object[k], ipath, value, track, ignore_error=ignore_error, _copy=False, logger=_logger, allow_create_path=allow_create_path)
            else:
                json_object[k] = value
        except Exception as e:
            err_msg = "Try to update {} but encountered {} => {}".format(track, type(e), e)
            if is_first or ignore_error:
                _logger.warn(err_msg)
            if not ignore_error:
                raise
        return json_object

    @staticmethod
    def static_update_value_of_path(json_object, path, value, ignore_error=True, logger=None, allow_create_path=False):
        if logger:
            _logger = logger
        else:
            _logger = VicJson.logger
        return VicJson.static_update_value_of_ipath(json_object, VicJson.path_to_ipath(path), value, ignore_error=ignore_error, logger=logger, allow_create_path=allow_create_path)

    @staticmethod
    def static_delete_ipath(json_object, ipath, track=None, ignore_error=True, _copy=True, logger=None):
        if logger:
            _logger = logger
        else:
            _logger = VicJson.logger
        is_first = False
        if not track:
            track = list()
            is_first = True
        if _copy:
            json_object = deepcopy(json_object)
        try:
            k = ipath.pop(0)
            track.append(k)
            if len(ipath) > 0:
                if isinstance(json_object, list):
                    k = int(k)
                VicJson.static_delete_ipath(json_object[k], ipath, track, ignore_error=ignore_error, _copy=False, logger=_logger)
            else:
                del json_object[k]
        except Exception as e:
            err_msg = "Try to delete {} but encountered {} => {}".format(track, type(e), e)
            if is_first or ignore_error:
                _logger.warn(err_msg)
            if not ignore_error:
                raise
        return json_object

    @staticmethod
    def static_delete_path(json_object, path, ignore_error=True, logger=None):
        if logger:
            _logger = logger
        else:
            _logger = VicJson.logger
        return VicJson.static_delete_ipath(json_object, VicJson.path_to_ipath(path), ignore_error=ignore_error, logger=_logger)

    def get_value_via_path(self, path):
        return jsonpath(self.json_object, path)

    def get_value_via_ipath(self, ipath):
        return self.get_value_via_path(self.ipath_to_path(ipath))

    def get_path_of_key(self, key=""):
        return jsonpath(self.json_object, "$..{}".format(key), result_type="PATH")

    def get_ipath_of_key(self, key=""):
        return jsonpath(self.json_object, "$..{}".format(key), result_type="IPATH")

    def get_value_of_key(self, key=""):
        return jsonpath(self.json_object, "$..{}".format(key))

    def get_path_of_value(self, value):
        matched_path = list()
        for path, _value in self.get_all_items().items():
            if isinstance(value, type(_value)) and value == _value:
                matched_path.append(path)
        return matched_path

    def get_path_of_item(self, key, value):
        matched_path = list()
        for path, _value in self.get_all_items().items():
            if isinstance(value, type(_value)) and value == _value:
                ipath = self.path_to_ipath(path)
                _key = ipath[-1]
                if key == _key:
                    matched_path.append(path)
        return matched_path

    def get_all_items(self):
        if self.need_update or not self._all_items:
            path = self.get_path_of_key()
            value = self.get_value_of_key()
            self._all_items = OrderedDict()
            for _ in range(len(path)):
                self._all_items[path[_]] = value[_]
            self.need_update = False
        return self._all_items

    def add_value_of_ipath(self, ipath, value, ignore_error=True):
        self.need_update = True
        self.json_object = self.static_add_value_of_ipath(self.json_object, ipath, value, ignore_error=ignore_error, logger=self.logger)

    def add_value_of_path(self, path, value, ignore_error=True):
        self.need_update = True
        self.json_object = self.static_add_value_of_path(self.json_object, path, value, ignore_error=ignore_error, logger=self.logger)

    def update_value_of_ipath(self, ipath, value, ignore_error=True):
        self.need_update = True
        self.json_object = self.static_update_value_of_ipath(self.json_object, ipath, value, ignore_error=ignore_error, logger=self.logger)

    def update_value_of_path(self, path, value, ignore_error=True):
        self.need_update = True
        self.json_object = self.static_update_value_of_path(self.json_object, path, value, ignore_error=ignore_error, logger=self.logger)

    def update_matched_key(self, key, new_value):
        matched_ipath = self.get_ipath_of_key(key)
        matched_ipath.reverse()
        for ipath in matched_ipath:
            self.update_value_of_ipath(ipath, new_value)

    def update_matched_value(self, old_value, value):
        matched_path = self.get_path_of_value(old_value)
        for path in matched_path:
            self.update_value_of_path(path, value)

    def update_matched_item(self, key, old_value, value):
        matched_path = self.get_path_of_item(key, old_value)
        for path in matched_path:
            self.update_value_of_path(path, value)

    def delete_ipath(self, ipath, ignore_error=True):
        self.need_update = True
        self.json_object = self.static_delete_ipath(self.json_object, ipath, ignore_error=ignore_error, logger=self.logger)

    def delete_path(self, path, ignore_error=True):
        self.need_update = True
        self.json_object = self.static_delete_path(self.json_object, path, ignore_error=ignore_error, logger=self.logger)

    def delete_matched_key(self, key):
        matched_ipath = self.get_ipath_of_key(key)
        matched_ipath.reverse()
        for ipath in matched_ipath:
            self.delete_ipath(ipath)

    def delete_matched_value(self, value):
        matched_path = self.get_path_of_value(value)
        for path in matched_path:
            self.delete_path(path)

    def delete_matched_item(self, key, value):
        matched_path = self.get_path_of_item(key, value)
        for path in matched_path:
            self.delete_path(path)


if __name__ == '__main__':
    d = '''
    {
        "index": {
            "number_of_shards": "1",
            "mapper": {
				"dynamic": "true"
			},
			"number of shards2": [{"number_of_shards": 99}],
            "number_of_replicas": 0,
            "analysis": {
                "9": {
                    "default": {
                        "type": "standard",
                        "stopwords": "_none_",
                        "number of shards2": [{"number_of_shards": 99}]
                    },
                    "number_of_shards": {"number_of_shards1": 99, "type": "standard"}
                }
            }
        }
    }
    '''
    j = VicJson(d)
    print(j)
    # _ = j.get_path_of_item("type", 'standard')
    # print(_)
    print("===========================================")
    # j.delete_ipath(["index", "analysis", "9", "default1"])
    # print(j)
    print("===========================================")
    j.add_value_of_ipath(["index", "analysis1", "9", "default", "type"], [], False)
    print(j)
    j.add_value_of_ipath(["index", "analysis1", "9", "default", "type", 0], 1, False)
    print(j)
    j.add_value_of_ipath(["index", "analysis1", "9", "default", "type", 0], 2, False)
    print(j)
    j.add_value_of_ipath(["index", "analysis1", "9", "default", "type", 2], 3, False)
    print(j)
    j.add_value_of_ipath(["index", "analysis1", "9", "default", "type"], [2, 1, 3], False)
    print(j)
    j.add_value_of_ipath(["script", "source"], "if (ctx._id == '') {ctx._id = 'null'}", False)
    print(j)
    j.update_value_of_ipath(["index", "analysis1", "9", "default", "type1"], [2, 1, 3], False)
    print(j)
    j.add_value_of_ipath(["test1"], {}, False)
    print(j)
    j.add_value_of_path("$.test2", {}, False)
    print(j)




