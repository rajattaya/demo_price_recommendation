PYTHON version: 3.6 and above
Dependencies: flask, pandas, numpy
Steps to run:
    set PYTHONPATH to the home of this directory(cd to the project directory then export PYTHONPATH=`pwd`)
    run  python app_server/app.py will launch a local host
    sample api request:
    http://127.0.0.1:5000/price_recommendation?distance=798&shipment_type=w2w&src_city=bogor&dst_city=pasuruan
    In order to run test run the following command:
        python test.py