# file_manager와 parking_spot_manager 모듈 import 하기
import file_manager as fm 
import parking_spot_manager as psm


def start_process(path):
    callList = fm.read_file(path) # path를 매개변수로 하여 file manager의 read_file 함수를 실행시킨다.
    useList = psm.str_list_to_class_list(callList) # callList를 str_list_to_class_list 함수를 통해 변환한다.
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            psm.print_spots(useList) # print_spots를 통해 출력하기
            # fill this block
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                useList = psm.filter_by_name(useList, keyword) # 기존 리스트를 keyword를 이용하여 필터 후 새로 저장
                # fill this block
            elif select == 2:
                keyword = input('type city:')
                useList = psm.filter_by_city(useList, keyword) # 기존 리스트를 keyword를 이용하여 필터 후 새로 저장
                # fill this block
            elif select == 3:
                keyword = input('type district:')
                useList = psm.filter_by_district(useList, keyword) # 기존 리스트를 keyword를 이용하여 필터 후 새로 저장
                # fill this block
            elif select == 4:
                keyword = input('type ptype:')
                useList = psm.filter_by_ptype(useList, keyword) # 기존 리스트를 keyword를 이용하여 필터 후 새로 저장
                # fill this block
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                locationsTuple = (min_lat, max_lat, min_lon, max_lon) # 입력받은 값들을 튜플로 저장
                useList = psm.filter_by_location(useList, locationsTuple) # 기존 리스트를 필터 후 새로 저장
                # fill this block
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:
            print("Exit")
            break # Exit 출력 후 반복 종료
            # fill this block
        else:
            print("invalid input")

start_process("./input/free_parking_spot.csv")