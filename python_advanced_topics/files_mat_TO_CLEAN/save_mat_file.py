"""
Adapted from https://kerpanic.wordpress.com/2017/11/21/save-out-python-numpy-data-as-mat-files-for-matlab/
https://subscription.packtpub.com/book/big-data-and-business-intelligence/9781786463517/12/ch12lvl1sec96/reading-and-writing-matlab-data-files

"""

                        # Create a dictionary
                        adict = {}
                        adict['transformed_ir'] = capture.transformed_ir
                        sio.savemat(os.path.join(an_output_path, img_write_filename_ir_mat), adict)