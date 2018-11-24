#! /usr/bin/python3

import os
import sys

#
def mkdir(path = './'):

	if not if_exists_then_do_nothing(path + 'include/'):
		os.mkdir(path + 'include/')
	
	if not if_exists_then_do_nothing(path + 'src/'):
		os.mkdir(path + 'src/')
		
	if not if_exists_then_do_nothing(path + 'build/'):
		os.mkdir(path + 'build/')

# 
def generate_main(path = './'):
	main_file = ( "" + 
		"/*\n" + 
		" * @description \n" + 
		" */\n\n" + 
		"#include <iostream>\n\n\n" + 
		"int main(int argc, char* argv[])\n" + 
		"{\n" + 
		'\tstd::cout << "Hello main !!!" << std::endl;' +
		"\t\n\n" + 
		"\treturn 0;\n" + 
		"}\n" )
		
	
	path = path + 'src/main.cpp'
	if not if_exists_then_do_nothing(path):
		with open(path, 'w') as fw:
			fw.write(main_file)
#
def generate_cmake(path = './'):
	cmake_file = ( "" 
		'cmake_minimum_required (VERSION 2.6)\n\n'
		'# project name\n'
		'project (project_name)\n\n'
		'# set compile flag\n'
		'# add_definitions ("-Wall -g")\n\n'
		'# set extern libraries\n'
		'# set (libraries libm.so)\n\n'
		'# set source directory\n'
		'aux_source_directory(src SRC_LIST)\n\n'
		'# head files\n'
		'include_directories(include)\n\n'
		'# set prefix\n'
		'set(ps_build_binary_prefix  "ps_")\n\n'
		'add_executable(${ps_build_binary_prefix}${PROJECT_NAME}  ${SRC_LIST})\n' )
	
	path = path + 'CMakeLists.txt'	
	
	if not if_exists_then_do_nothing(path):
		with open(path, 'w') as fw:
			fw.write(cmake_file)
			
#
def generate_header(file, path = './'):
	path = path + 'include/' + file + ".h"
	
	class_header_file = (''
		'/*\n'
		' * @description \n'
		' */\n\n'
		'#ifndef ' + file.upper() + '_H_\n'
		'#define ' + file.upper() + '_H_\n\n\n'
		'class ' + file + '//: public SOMECLASS\n'
		'{\n'
		'private: \n\n\n'
		'public: \n'
		'\t'  + file + '();\n'
		'\t~' + file +  '();\n\n\n'
		'};\n\n\n'
		'#endif\n' )
		
				  
	if not if_exists_then_do_nothing(path):
		with open(path, 'w') as fw:
			fw.write(class_header_file)
			
#
def generate_class(file, path = './'):
	path = path + 'src/' + file + ".cpp"
	
	class_header_file = (''
		'/*\n'
		' * @description \n'
		' */\n\n'
		'#include "' + file + '.h"\n\n\n'
		'' + file + '::'  + file + '()\n{\n\t\n}\n\n'
		'' + file + '::~' + file +  '()\n{\n\t\n}\n\n')
		
				  
	if not if_exists_then_do_nothing(path):
		with open(path, 'w') as fw:
			fw.write(class_header_file)
#
def deal_argv(argv):
	if argv[0] == 'main':
		generate_main()
		generate_cmake()
	if argv[0] == 'class' and len(argv) >= 2:
		for file in argv[1:]:
			generate_header(file)
			generate_class(file)
		
#
def if_exists_then_do_nothing(path):
	if os.path.exists(path):
		print("The file has exists: " + path)
		return True
	else:
		return False
		


###################################################################

if __name__ == '__main__':
	argv = sys.argv[1:]
	argc = len(argv)
	
	mkdir()
	
	if argc == 0:
		generate_main()
		generate_cmake()
	else:
		deal_argv(argv)
