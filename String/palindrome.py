from Data_Structure.list_node import ListNode

class Palindrome:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        if not head.next:
            return True

        cur: ListNode = head
        stack_1: List = [-1]
        stack_2: List = []
        while cur:
            if cur.val != stack_1[-1]:
                if cur.next and cur.next.val == stack_1[-1]:
                    stack_2.append(cur.val)
                    cur = cur.next
                    continue
                while stack_2:
                    stack_1.append(stack_2.pop())
                stack_1.append(cur.val)
                cur = cur.next
                continue
            else:
                temp_val = stack_1.pop()
                for i in range(2):
                    stack_2.append(temp_val)
                cur = cur.next
                continue

        if len(stack_1) == 1 and stack_1[-1] == -1:
            return True
        else:
            return False


# # This is a sample Python script.

# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# from String.palindrome import Palindrome
# from Data_Structure.list_node import ListNode

# if __name__ == '__main__':

#     head: ListNode = ListNode(val=1)
#     head.next = ListNode(val=0)
#     head.next.next = ListNode(val=1)

#     solution = Palindrome()
#     res = solution.isPalindrome(head)
#     print(res)
