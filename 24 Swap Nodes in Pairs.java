
/**
 * Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        if(head == null || head.next == null)return head;
        ListNode d = new ListNode(0), a;
        d.next = head;
        a=d;
        while(head!=null&&head.next!=null) {
            a.next = head.next;
            head.next = head.next.next;
            a.next.next = head;
            a = a.next.next;
            head =  head.next;
        }
        return d.next;
    }
}