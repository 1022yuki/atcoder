# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Optional, List
T = TypeVar('T')

class SortedMultiset(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a=None) -> None:
        "Evenly divide `a` into buckets."
        if a is None: a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size] for i in range(bucket_size)]
    
    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
        a = list(a)
        if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
            a = sorted(a)
        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j
    
    def __len__(self) -> int:
        return self.size
    
    def __repr__(self) -> str:
        return "SortedMultiset" + str(self.a)
    
    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _find_bucket(self, x: T) -> List[T]:
        "Find the bucket which should contain x. self must not be empty."
        for a in self.a:
            if x <= a[-1]: return a
        return a

    def __contains__(self, x: T) -> bool:
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        return i != len(a) and a[i] == x

    def count(self, x: T) -> int:
        "Count the number of x."
        return self.index_right(x) - self.index(x)

    def add(self, x: T) -> None:
        "Add an element. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a = self._find_bucket(x)
        insort(a, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i == len(a) or a[i] != x: return False
        a.pop(i)
        self.size -= 1
        if len(a) == 0: self._build()
        return True

    def lt(self, x: T) -> Optional[T]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Optional[T]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Optional[T]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Optional[T]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]
    
    def __getitem__(self, x: int) -> T:
        "Return the x-th element, or IndexError if it doesn't exist."
        if x < 0: x += self.size
        if x < 0: raise IndexError
        for a in self.a:
            if x < len(a): return a[x]
            x -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans

N, K, Q = map(int, input().split())
X = []
Y = []
for i in range(Q):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

if N==1:
    for i in range(Q):
        print(Y[i])
    exit()

if N==K:
    ans = 0
    li = [0]*N
    for i in range(Q):
        ans -= li[X[i]-1]
        li[X[i]-1] = Y[i]
        ans += li[X[i]-1]
        print(ans)
    exit()

ans = 0
li = [0]*N
# 上からK個のマルチセット
m_set_use = SortedMultiset([0]*K)
# 上からK個以外のマルチセット
m_set_unuse = SortedMultiset([0]*(N-K))
# print(m_set)
for i in range(Q):
    
    # すでにms_useに入っている数字が更新される
    if li[X[i]-1] in m_set_use:     
      # print('A')
      # useの最小値を削除しunuseに追加する場合
      ans -= li[X[i]-1]
      m_set_use.discard(li[X[i]-1])
      # unuseの最大値をuseに追加
      ans += Y[i]
      m_set_use.add(Y[i])
      
      if Y[i] < m_set_unuse[-1]:
          ans -= Y[i]
          m_set_use.discard(Y[i])
          m_set_unuse.add(Y[i])
          ans += m_set_unuse[-1]
          m_set_use.add(m_set_unuse[-1])
          m_set_unuse.discard(m_set_unuse[-1])

    else:
        # print('B')
        # unuse側を更新
        m_set_unuse.discard(li[X[i]-1])
        m_set_unuse.add(Y[i])
        # useの最小値を削除しunuseに追加する
        ans -= m_set_use[0]
        m_set_unuse.add(m_set_use[0])
        m_set_use.discard(m_set_use[0])
        # unuseの最大値をuseに追加
        ans += m_set_unuse[-1]
        m_set_use.add(m_set_unuse[-1])
        m_set_unuse.discard(m_set_unuse[-1])

    li[X[i]-1] = Y[i]
    # print(li)
    # print(m_set_use)
    # print(m_set_unuse)
    print(ans)
    # print()