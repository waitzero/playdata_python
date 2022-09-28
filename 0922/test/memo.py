import os

def mk_dir(name):
    if not os.path.isdir(name): #디렉토리가 없으면
        os.mkdir(name)
        print(name, '디렉토리가 생성되었음')

def select_file(dname):
    files = os.listdir(dname)# 디렉토리 파일 목록
    for idx, f in enumerate(files):
        print(idx,'.',f)
    num = int(input('읽거나 삭제할 파일 번호를 입력'))
    if 0<=num<len(files):
        return files[num]

def read_file(dname):
    fname = select_file(dname)
    if fname==None:
        print('잘못된 번호')
    else:
        path = dname+'/'+fname
        f = open(path, 'r', encoding='utf-8')
        content = f.read()
        print(content)

def check_filename(dname):
    # 디렉토리의 파일 목록 읽음
    flist = os.listdir(dname)
    # 쓰기할 파일명 입력
    fname = input('파일명 입력')
    # 오픈 모드 저장
    mode = 'w'
    while fname in flist: #중복된 이름
        m = input('중복된 파일명 1.다시입력 2.덮어쓰기 3.이어쓰기')
        if m=='1':
            fname = input('파일명 입력')
        elif m == '2':
            break
        elif m=='3':
            mode = 'a'
            break
    return fname, mode

# 파일 쓰기 함수
def write_file(dname):
    # 파일명 입력 및 중복 체크해서 결과를 fname, mode저장
    fname, mode = check_filename(dname)

    # 오픈할 파일 경로: '디렉토리명/파일명'
    path = dname+'/'+fname

    # 파일 쓰기 모드 오픈
    f = open(path, mode, encoding='utf-8')
    while True:
        content = input('파일 내용 입력. 루프 나가려면 /stop')
        if content == '/stop':
            break
        # 파일쓰기
        f.write(content+'\n')
    f.close()

def del_file(dname):
    fname = select_file(dname)
    if fname==None:
        print('잘못된 번호')
    else:
        os.remove(dname+'/'+fname)

if __name__=='__main__':
    dname = 'memo'
    mk_dir(dname    )
    while True:
        m = input('1.읽기 2.쓰기 3.삭제 4.종료')
        if m=='1':
            read_file(dname)
        elif m=='2':
            write_file(dname)
        elif m=='3':
            del_file(dname)
        elif m=='4':
            break