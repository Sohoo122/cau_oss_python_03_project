class parking_spot:
    # you have to implement 'constructor(생성자)' and 'get' method
    def __init__(self, name, city, district, ptype, longitude, latitude) :
       self.__item = {
           'name' : name,
           'city' : city,
           'district' : district,
           'ptype' : ptype,
           'longitude' : longitude,
           'latitude' : latitude
       } # __item 딕셔너리를 6개의 인수를 통해 선언한다.

    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s

    def get(self, keyword = 'name') :
        return self.__item[keyword] # 받은 keyword 인수를 통해 __item[keyword]에 해당하는 값을 반환한다.


def str_list_to_class_list(str_list) :
    returnTmp = list()
    retList = list()
    for i in range(0, len(str_list)) :
        txtTmp = str(str_list[i]) # txtTmp에 str_list 리스트 요소 하나를 저장한다.
        returnTmp = txtTmp.split(',') # split을 이용하여 쉼표 기준으로 잘라 리스트를 생성한다.
        retList.append(parking_spot(returnTmp[1], returnTmp[2], returnTmp[3], returnTmp[4], returnTmp[5], returnTmp[6])) # return 할 retList에 순번인 returnTmp[0]를 제외하고 parking_spot의 리스트로 변환 후 append한다.
    return retList 


def print_spots(spots) :
    print(f"---print elements({len(spots)})")
    for i in range(0, len(spots)) :
        call = parking_spot.__str__(spots[i]) # call에 parking_spot의 메소드 __str__을 spots[i]를 매개변수로 하여 저장한다.
        print(call) # 바로 call을 print, for문으로 spots의 모든 요소를 끝까지 출력한다.


def filter_by_name(spots, name) :
    retList = [spots[i] for i in range (0, len(spots)) if (name in parking_spot.get(spots[i], 'name')) == True] # for문과 parking_spot.get을 통해 spots[i]에 매개변수 name이 포함되어 있는지 확인 후 True라면 retList에 저장
    return retList

def filter_by_city(spots, city) :
    retList = [spots[i] for i in range (0, len(spots)) if (city in parking_spot.get(spots[i], 'city')) == True] # for문과 parking_spot.get을 통해 spots[i]에 매개변수 city가 포함되어 있는지 확인 후 True라면 retList에 저장
    return retList
def filter_by_district(spots, district) :
    retList = [spots[i] for i in range (0, len(spots)) if (district in parking_spot.get(spots[i], 'district')) == True] # for문과 parking_spot.get을 통해 spots[i]에 매개변수 district이 포함되어 있는지 확인 후 True라면 retList에 저장
    return retList

def filter_by_ptype(spots, ptype) :
    retList = [spots[i] for i in range (0, len(spots)) if (ptype in parking_spot.get(spots[i], 'ptype')) == True] # for문과 parking_spot.get을 통해 spots[i]에 매개변수 ptype이 포함되어 있는지 확인 후 True라면 retList에 저장
    return retList

def filter_by_location(spots, locations) :
    retList = [spots[i] for i in range (0, len(spots)) 
               if (float(parking_spot.get(spots[i], 'latitude')) > float(locations[0])) 
               and (float(parking_spot.get(spots[i], 'latitude')) < float(locations[1])) 
               and (float(parking_spot.get(spots[i], 'longitude')) > float(locations[2]))
               and (float(parking_spot.get(spots[i], 'longitude')) < float(locations[3]))
               ] # for문과 parking_spot.get을 통해 spots[i]의 값들이 각각 최대, 최솟값 사이에 있는 지 확인 후 맞다면 저장
    return retList

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
# if __name__ == '__main__':
#     print("Testing the module...")
#     # version#2
#     import file_manager
#     str_list = file_manager.read_file("./input/free_parking_spot.csv")
#     spots = str_list_to_class_list(str_list)
#     print_spots(spots)

#     # version#3
#     spots = filter_by_district(spots, '동작')
#     print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)