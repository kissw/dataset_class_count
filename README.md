## Data Augmentation

Dataset에서 Class별 데이터의 개수를 보는 프로그램.  
Dataset 폴더안에 text 파일이 있어야됨.  </br></br>

## 사용법
### 파라미터
```yaml
dataset_path: ./img #데이터셋 경로 
some_dict: {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0} # 클래스번호 : 초기값(0).
```
```yaml
person: 	0
bicycle:    1
car:	    2
motorcycle:	3
truck:	    4
dog:	    5

```
</br>
</br>

### 명령어
conda 환경설치 방법은 상위 폴더를 참조
```
(base) $ conda activate 3w

(3w) $ python src/dataset_class_count.py
```