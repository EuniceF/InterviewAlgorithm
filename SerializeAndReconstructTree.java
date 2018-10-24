import java.util.LinkedList;
import java.util.Queue;

public class SerializeAndReconstructTree {

    public static class Node {
        public int value;
        public Node left;
        public Node right;

        public Node(int data) {
            this.value = data;
        }
    }

    // serialization
    public static String serialByPre(Node head) {
        if (head == null) {
            return "#_";
        }
        String res = head.value + "_";
        res += serialByPre(head.left);
        res += serialByPre(head.right);
        return res;
    }

    // de-serialization
    public static Node reconByPreString(String preStr) {
        String[] values = preStr.split("_");
        Queue<String> queue = new LinkedList<String>();
        for (String v : values) {
            queue.offer(v);
        }
        return reconPreOrder(queue);
    }

    public static Node reconPreOrder(Queue<String> queue) {
        String value = queue.poll();
        if (value.equals("#")) {
            return null;
        }
        Node head = new Node(Integer.valueOf(value));
        head.left = reconPreOrder(queue);
        head.right = reconPreOrder(queue);
        return head;
    }

    public static String serialByLevel(Node head) {
        if (head == null) {
            return "#_";
        }
        String res = head.value + "_";
        Queue<Node> queue = new LinkedList<Node>();
        queue.offer(head);
        while (!queue.isEmpty()) {
            head = queue.poll();
            if (head.left != null) {
                queue.offer(head.left);
                res += head.left.value + "_";
            } else {
                res += "#_";
            }
            if (head.right != null) {
                queue.offer(head.right);
                res += head.right.value + "_";
            } else {
                res += "#_";
            }
        }
        return res;
    }

    public static Node reconByLevelString(String levelStr) {
        String[] values = levelStr.split("_");
        Queue<Node> queue = new LinkedList<Node>();
        int index = 0;
        Node head = generateNodeByString(values[index++]);
        if (head != null) {
            queue.offer(head);
        }
        Node curr = null;
        while (!queue.isEmpty()) {
            curr = queue.poll();
            curr.left = generateNodeByString(values[index++]);
            curr.right = generateNodeByString(values[index++]);
            if (curr.left != null) {
                queue.offer(curr.left);
            }
            if (curr.right != null) {
                queue.offer(curr.right);
            }
        }
        return head;
    }

    public static Node generateNodeByString(String val) {
        if (val.equals("#")) {
            return null;
        }
        return new Node(Integer.valueOf(val));
    }
    
    public static void printpreOrder(Node head) {
        if (head == null) {
            return; 
        }
        System.out.print(head.value + " ");
        printpreOrder(head.left);
        printpreOrder(head.right);
    }

    public static void main(String[] args) {
		Node head = new Node(1);
		head.left = new Node(2);
		head.right = new Node(3);
		head.left.left = new Node(4);
        head.right.right = new Node(5);
        String pre = serialByPre(head);
        System.out.println(pre); 
        String level = serialByLevel(head);
        System.out.println(level);
        
        // Node head2 = reconByPreString(pre);
        // System.out.println("reconstruct by pre String: ");
        // printpreOrder(head2);
        Node head2 = reconByLevelString(level);
        System.out.println("reconstruct by level string");
        printpreOrder(head2);
    }
}