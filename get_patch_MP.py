import multiprocessing
import argparse
import util_multi
import glob

# argparse
parser = argparse.ArgumentParser()
parser.add_argument('--slide_path', required=True, type=str, help='Input the target slide path.')
parser.add_argument('--level', required=True, type=int, help='Input the level of target slide.')
parser.add_argument('--patch_size', default=512, type=int, help='Input the image shape.')
parser.add_argument('--magnification',required=True, type=int, help='Input the magnification of the patch.')
parser.add_argument('--save_patch_path', required=True, type=str, help='Input the patch path that will be saved.')

# argparse to variable
args = parser.parse_args()
slide_path = args.slide_path
level = args.level
patch_size = args.patch_size
save_patch_path = args.save_patch_path
magnification = args.magnification

# init_params setting
init_params = {
    'svs_path' : '',
    'xml_path' : '',
    'level' : level,
    'patch_size' : patch_size,
    'save_patch_path' : save_patch_path            
}

# svsfile_to_patch extrcator
def extract(init_params, magnification=magnification):
    slide = util_multi.processor(init_params)
    slide.get_patch(magnification=magnification, save=True)

# slide_alth and list setting
slide_path = slide_path + '*.svs' 
svs_list = glob.glob(slide_path)

# using multiprocess 
for svs_path in svs_list:
    xml_path = '.'.join(svs_path.split('.')[:-1]) + '.xml'
    init_params.update({'svs_path':svs_path, 'xml_path':xml_path})
    p = multiprocessing.Process(target=extract, args=(init_params,))
    p.start()