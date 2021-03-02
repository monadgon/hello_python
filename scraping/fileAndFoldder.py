# https://wikidocs.net/39 하위 디렉토리 검색하기
import os
def file_worker(target_path):
    i = 0
    for (path, dir, files) in os.walk(target_path):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.sql':
                fullpath = "%s/%s" %(path, filename)
                print(fullpath)
                f = open(fullpath, 'r', encoding='UTF-8')
                data = f.read()
                print(data)
                i = 1
            if i == 1:
                break
        if i == 1:    
            break
            #print("%s/%s" % (path, filename))

file_worker("D:\\pjt_plm\\db_migration_to_pg\\sql\\postgre_NEADAM\\dml")