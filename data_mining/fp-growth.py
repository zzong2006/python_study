"""
    fp-growth algorithm

"""
import csv
from collections import defaultdict


class FPNode:  # Trie 구조와 상당히 흡사
    def __init__(self, parent=None, val=None):
        self.table = defaultdict(FPNode)
        self.count = defaultdict(int)
        self.parent = parent
        self.value = val

    def insert(self, input_data: list, freq_table):
        curr = self
        for a in input_data:
            curr.count[a] += 1
            if a not in curr.table:  # 노드가 새로 생성될 경우에만 포인터를 넣어줌
                freq_table[a].append(curr.table[a])
                curr.table[a].value = a
                curr.table[a].parent = curr
            curr = curr.table[a]


class FPTree:
    def __init__(self, transactions, th):
        self.frequency = self.count_total_frequency(transactions, th)
        self.item_table = defaultdict(list)
        self.root = FPNode(None, None)
        self.build_tree(transactions)

    def build_tree(self, transactions):
        """
        주어진 transactions을 기반으로 fp-tree를 만듦
        """
        for t in transactions:
            new_u = list(filter(lambda x: x in self.frequency, t))  # threshold 미만의 아이템은 제거
            sorted_u = sorted(new_u, key=lambda x: self.frequency[x], reverse=True)  # item count에 의한 내림차순 정렬
            if sorted_u:
                self.root.insert(sorted_u, self.item_table)

    def has_single_route(self, curr):
        """
        Tree가 single path를 가지고 있는지 확인함
        :param curr: root node
        """
        n = len(curr.table)
        if n > 1:
            return False
        elif n == 0:
            return True
        else:
            single_key = next(self.table.keys())
            next_curr = self.table[single_key]
            return self.has_single_route(next_curr)

    def find_combinations(self, th):
        if self.has_single_route(self.root):
            return self.generate_combinations(th)
        else:
            return self.multi_path(th)

    def generate_combinations(self, th):
        sorted_list = sorted(self.frequency.keys(), key=lambda x: self.frequency[x])

        pass

    def multi_path(self, th):
        sorted_list = sorted(self.frequency.keys(), key=lambda x: self.frequency[x])
        for x in sorted_list:
            sub_trans = []
            for node in self.item_table[x]:
                sub_trans.append(FPTree.get_single_trans(node.parent))
            sub_tree = FPTree(sub_trans, th)
            patterns = sub_tree.find_combinations(th)

        return None

    @classmethod
    def get_single_trans(self, node):
        ls = []
        while node.value:
            ls.append(node.value)
            node = node.parent

        return ls

    def count_total_frequency(self, u_info: list, th: int, verbose: bool = True):
        """
        item frequency를 계산하고 임계치 미만의 아이템은 계산 정보에서 제외
        :param verbose: 삭제 정보 표기 여부
        :param u_info: 사용자 정보
        :param th: 최소 임계치 수
        :return: item frequency
        """
        freq = defaultdict(int)

        for u in u_info:
            for item in u:
                freq[item] += 1

        before = len(freq.keys())

        for k in list(freq.keys()):  # iterator를 freq.keys()로 하면 key 삭제 시, 에러 발생
            if freq[k] < th:
                del freq[k]
        after = len(freq.keys())

        if verbose:
            print('총 {} 개의 item이 threshold {} 에 못미쳐서 삭제됨'.format(before - after, threshold))

        return freq



