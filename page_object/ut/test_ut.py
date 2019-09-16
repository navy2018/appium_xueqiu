import yaml

class TestYaml(object):

    def test_yaml(self):
        dict=yaml.load(open('../data/LoginPage.yaml','r'))  #最开始运行出错，发现是yaml文件写错了，少写了一个空格
        print(dict)
        for step in dict["loginByPassword"]:
            print(step)
            print(step['locator'])