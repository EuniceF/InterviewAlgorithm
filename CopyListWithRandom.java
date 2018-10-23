import java.util.HashMap;

public class CopyListWithRandom {
    public static class Node {
        public int value;
        public Node next;
        public Node random;

        public Node(int data) {
            this.value = data;
        }
    }

    // use hashmap
    public static Node copyListWithRand1(Node head) {
        HashMap<Node, Node> map = new HashMap<Node, Node>();
        Node curr = head;
        while (curr != null) {
            map.put(curr, new Node(curr.value));
            curr = curr.next;
        }
        curr = head;
        while (curr != null) {
            map.get(curr).next = map.get(curr.next);
            map.get(curr).random = map.get(curr.random);
            curr = curr.next;
        }
        return map.get(head);
    }

    //copy without hashmap
    public static Node copyListWithRand2(Node head) {
        if (head == null) {
            return null;
        }
        Node curr = head;
        Node tmp = null;
        // copy node and link to every node
        while (curr != null) {
            tmp = new Node(curr.value);
            tmp.next = curr.next;
            curr.next = tmp;
            curr = curr.next.next;
        }
        // connect random
        curr = head;
        while (curr != null) {
            curr.next.random = curr.random != null ? curr.random.next : null;
            curr = curr.next.next;
        }
        // split
        Node res = head.next;
        Node nodeCopy = null;
        curr = head;
        while (curr != null) {
            tmp = curr.next.next;
            nodeCopy = curr.next;
            nodeCopy.next = tmp != null ? tmp.next : null;
            curr.next = tmp;
            curr = tmp;
        }
        return res;
    }

    // print list
    public static void printRandLinkedList(Node head) {
        Node curr = head;
        System.out.print("order: ");
        while (curr != null) {
            System.out.print(curr.value + " ");
            curr = curr.next;
        }
        System.out.println();
        curr = head;
        System.out.print("random: ");
        while (curr != null) {
            System.out.print(curr.random == null ? " - " : curr.random.value + " ");
            curr = curr.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Node head = null;
		Node res1 = null;
		Node res2 = null;
		printRandLinkedList(head);
		res1 = copyListWithRand1(head);
		printRandLinkedList(res1);
		res2 = copyListWithRand2(head);
		printRandLinkedList(res2);
		printRandLinkedList(head);
		System.out.println("=========================");

		head = new Node(1);
		head.next = new Node(2);
		head.next.next = new Node(3);
		head.next.next.next = new Node(4);
		head.next.next.next.next = new Node(5);
		head.next.next.next.next.next = new Node(6);

		head.random = head.next.next.next.next.next; // 1 -> 6
		head.next.random = head.next.next.next.next.next; // 2 -> 6
		head.next.next.random = head.next.next.next.next; // 3 -> 5
		head.next.next.next.random = head.next.next; // 4 -> 3
		head.next.next.next.next.random = null; // 5 -> null
		head.next.next.next.next.next.random = head.next.next.next; // 6 -> 4

		printRandLinkedList(head);
		res1 = copyListWithRand1(head);
		printRandLinkedList(res1);
		res2 = copyListWithRand2(head);
		printRandLinkedList(res2);
		printRandLinkedList(head);
		System.out.println("=========================");
    }
}