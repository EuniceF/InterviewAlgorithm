public class Array_To_Stack_Queue {

    public static class ArrayStack {
        private Integer[] arr;
        private Integer size;

        public ArrayStack(int initsize) {
            if (initsize < 0) {
                throw new IllegalArgumentException("The init size is less than 0!");
            }
            arr = new Integer[initsize];
            size = 0;
        }

        public Integer peek() {
            if (size == 0) {
                return null;
            }
            return arr[size - 1];
        }

        public void push(int obj) {
            if (size == arr.length) {
                throw new ArrayIndexOutOfBoundsException("The stack is full!");
            }
            arr[size++] = obj;
        }

        public Integer pop() {
            if (size == 0) {
                throw new ArrayIndexOutOfBoundsException("The stack is empty!");
            }
            return arr[--size];
        }
    }

    public static class ArrayQueue {
        private Integer[] arr;
        private Integer size;
        private Integer first;
        private Integer last;

        public ArrayQueue(int initsize) {
            if (initsize < 0) {
                throw new IllegalArgumentException("Initial size is less than 0!");
            }
            arr = new Integer[initsize];
            size = 0;
            first = 0;
            last = 0;
        }

        public Integer peek() {
            if (size == 0) {
                return null;
            }
            return arr[first];
        }

        public void push(int obj) {
            if (size == arr.length) {
                throw new ArrayIndexOutOfBoundsException("The queue is full!");
            }
            size++;
            arr[last] = obj;
            last = last == arr.length - 1 ? 0 : last + 1;
        }

        public Integer poll() {
            if (size == 0) {
                throw new ArrayIndexOutOfBoundsException("THe queue is empty!");
            }
            size--;
            index = first;
            first = fist = arr.length - 1 ? 0 : first + 1;
            return arr[index];
        }
    }

    public static void main(String[] args) {
        
    }
    
}