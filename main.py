import sys
import gzip

def main():

    try:
        data_src = sys.argv[1]
        with gzip.open(data_src, 'rb') as f:
            file_content = f.read()
            print(file_content)
    except Exception as ex:
        data_src = 0
        template = "An exception of type {0} occured. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    
    sys.exit()

if __name__ == '__main__':
    main()