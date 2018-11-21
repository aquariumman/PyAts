

"""
You can run the test with

easypy job_03.py -testbed_file testbed.yaml     --- will run test with default parameters

or

easypy job_03.py -testbed_file testbed.yaml -user_vm  (users' name on vm)  -- there is default value
                                            -ip_vm (vm's ip we are connecting to) -- there is default value
                                            -filename (filename for our file which we will work with) -- there is default value

"""


from pyats.aetest import Testcase, test, setup,	cleanup, main
from pyats.utils.fileutils import FileUtils
from pyats.topology.loader import load
import os

testbed =load('testbed.yaml')


class Test(Testcase):
    @setup
    def connection(self, testbed, username_vm, filename):
        self.vm_path = f'sftp://localhost/home/{username_vm}'
        self.host_path = os.getcwd()
        try:
            #open((os.getcwd().join('/').join(filename)), 'a').write('test text for file on localhost').close()
            with open(f'{self.host_path}/{filename}', 'a') as f:
                f.write('test text for file on localhost')
                f.close()
        except:
            print('Something went wrong while creating a file while creating file on local host')
            self.failed('because of error while creating file on host!!')

        self.vm = testbed.devices['vm']
        self.vm.connect()
        self.vm.execute('hostname')
        self.vm.execute('ping -c 2 8.8.8.8')
        self.vm.execute('cd /home/pyast')

        try:
            #self.vm.execute("open('/home/pyast/file_on_remote_vm', 'a') as f:f.write('test text for file on remote vm'); f.close()")
            self.vm.execute(f'touch /home/{username_vm}/{filename}')
        except:
            print('Something went wrong while creating a file while creating file on remote vm')
            self.failed('because of error while creating file on remote vm!!')

        self.passed('We have not errors so test passed!')



    @test
    def copy_file_from_host_to_vm(self, ip_vm, filename, username_vm):
        try:
            with FileUtils(testbed=testbed) as futils:
                futils.copyfile(
                    source=f'{self.host_path}/{filename}',
                    destination=f'sftp://{ip_vm}/home/{username_vm}/received_from_host_{filename}'
                )
        except:
            print('while copying file from host to vm...something went wrong')



    @test
    def copy_file_from_vm_to_host(self, ip_vm, filename, username_vm):
        try:
            with FileUtils(testbed=testbed) as futils:
                futils.copyfile(
                    source =f'sftp://{ip_vm}/home/{username_vm}/{filename}',
                    destination = f'{self.host_path}/received_from_remotevm_{filename}'
                )
        except:
            print('while copying file from vm to host...something went wrong')


    @test
    def check_file_existense(self, filename, ip_vm, username_vm):
        try:
            if os.path.exists(f'{self.host_path}/received_from_remotevm_{filename}') and self.vm.execute(f'ls -la /home/pyast/received_from_host_{filename}'):
                print('*****************************************************************File is received on host comp')
            with FileUtils(testbed=testbed) as futils:
                if futils.checkfile(f'sftp://{ip_vm}/home/{username_vm}/received_from_host_{filename}'):
                    print('**************************************************************File is received on remote vm')
                else:
                    raise Exception
        except:
            print("Something went wrong while checking copied files")
        self.passed('Files are copied correctly')



    @cleanup
    def cleanup(self, ip_vm, filename, username_vm):
        try:
            with FileUtils(testbed=testbed) as futils:
                futils.deletefile(f'sftp://{ip_vm}/home/{username_vm}/{filename}')
                futils.deletefile(f'sftp://{ip_vm}/home/{username_vm}/received_from_host_{filename}')
                # futils.deletefile(target=f'{self.host_path}/received_from_remotevm_{filename}')
                # futils.deletefile(target=f'{self.host_path}/{filename}')
            os.remove(f'{self.host_path}/received_from_remotevm_{filename}')
            os.remove(f'{self.host_path}/{filename}')
            print("=========================test files were deleted on both machines")
        except:
            print("Somthing went wrong while deleting a files...")
            self.passx("I think it is passed")


        try:
            self.vm.disconnect_all()
        except:
            print("Somthing went wrong while disconnect all..")
            self.passx("I think it is passed")

        self.passed('Cleanup is done')


if __name__=="__main__":
    testbed = load('testbed.yaml')
    main(testbed=testbed)