# 한글 깨짐

# 1. 터미널 한글깨짐

`vim ~/.bashrc` 에서 아래 코드를 추가.
```
LANG="ko_KR.UTF-8"
export LANG="ko_KR.UTF-8"
```

`source ~/.bashrc` 를 입력하여 적용.

출처: https://goni9071.tistory.com/150

# 2. vim 한글깨짐

`vim ~/.vimrc` 에서 아래 코드를 추가합니다.


```
set encoding=utf-8
set fileencodings=utf-8,euc-kr
```

출처: https://goni9071.tistory.com/150
