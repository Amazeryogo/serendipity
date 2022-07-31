from backend import *
import waitress

if __name__ == "__main__":
    print('Serendipity v1.0 \n By Suvid Datta \n This software comes with NO WARRANTY WHATSOEVER \n \n \n')
    waitress.serve(app, host='0.0.0.0', port=8080)
