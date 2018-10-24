import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class IsBSTAndCBT {

    public static class Node {
        public int value;
        public Node left;
        public Node right;

        public Node(int data) {
            this.value = data;
        }
    }

    public static boolean isBST(Node head) {
        if (head == null) {
            return true;
        }
        int preValue = Integer.MIN_VALUE;
        Stack<Node> stack = new Stack<Node>();
        while (!stack.isEmpty() || head != null) {
            if (head != null) {
                stack.push(head);
                head = head.left;
            } else {
                head = stack.pop();
                preValue = Math.max(preValue, head.value);
                // System.out.print(preValue);
                if (head.value != preValue) {
                    return false;
                }
                head = head.right;
            }
        } 
        return true;
    }

    public static boolean isCBT(Node head) {
        if (head == null) {
            return true;
        }
        boolean leaf = false;
        Queue<Node> queue = new LinkedList<Node>();
        queue.offer(head);
        while (!queue.isEmpty()) {
            head = queue.poll();
            if ((head.left == null && head.right != null) || (leaf && (head.left != null || head.right != null))) {
                return false;
            }
            if (head.left != null) {
                queue.offer(head.left);
            }
            if (head.right != null) {
                queue.offer(head.right);
            } else {
                leaf = true;
            }
        }
        return true;
    }

    public static void main(String[] args) {
		Node head = new Node(4);
		head.left = new Node(2);
		head.right = new Node(6);
		head.left.left = new Node(1);
		head.left.right = new Node(3);
        head.right.left = new Node(5);
        
        System.out.println(isBST(head));
        System.out.println(isCBT(head));
    }
}