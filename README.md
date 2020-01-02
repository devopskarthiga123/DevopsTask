## Install Ansible

$ sudo apt-get update
$ sudo apt-get install software-properties-common
$ sudo apt-add-repository ppa:ansible/ansible
$ sudo apt-get update
$ sudo apt-get install ansible

## Clone Ansible Scripts Repository

$ git clone 

## Clone Ansible Scripts Repository

Note:
$  Security group "AllowSSH" and keypair "newkeys" should be created before you run this playbook
$  Inaddition -Image, region and subnet needs to be provided in group_vars.

$ sudo nano group_vars/main.yml

### To create ec2-instance with python dependencies

$ sudo ansible-playbook aws-ec2.yml --ask-pass

### Python script to list all instances that belong to particular AWS account

$ sudo ansible-playbook  list_instances.py --ask-pass

### Python script to list only t2 medium instances on AWS account

$ sudo ansible-playbook  listt2medim_instances.py --ask-pass
