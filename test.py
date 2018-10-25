import argparse
parser = argparse.ArgumentParser()

#-db DATABSE -u USERNAME -p PASSWORD -size 20
parser.add_argument("-f", "--input_folder",dest="input_folder", help="Database name")
parser.add_argument("-o", "--output_folder",dest="output_folder", help="User name")


args = parser.parse_args()
print(args)

print( "input folder {} output folder {} ".format(args.input_folder, args.output_folder))