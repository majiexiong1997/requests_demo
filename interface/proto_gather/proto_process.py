import os

#批量转换proto文件

path = r'C:\Users\majiexiong\PycharmProjects\requests_demo\interface\protobuf_file'
files = os.listdir(path)





def change_proto_to_pb(path):
    proto_list = os.listdir(path)
    proto_list.pop(-1)
    for proto_file in proto_list:

        os.system('protoc -I={} --python_out={} {}'.format(path, path, proto_file))



if __name__ == '__main__':
    change_proto_to_pb(path)