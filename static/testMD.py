import markdown2

testString = """

> ## This is a header.
>
> 1.   This is the first list item.
> 2.   This is the second list item.
>
> Here's some example code:
>
>     return shell_exec("echo $input | $markdown_script");
>
>     yum install -y http://mirrors.aliyun.com/centos/7/cloud/x86_64/openstack-newton/centos-release-openstack-newton-1-1.el7.noarch.rpm
>     yum install -y openvswitch
>

"""
testMD = markdown2.markdown(testString)

print(testMD)ostream