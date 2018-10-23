import java.util.Arrays;
import java.util.Comparator;

public class Comparator1 {

    public static class Student {
        public String name;
        public int id;
        public int age;

        public Student (String name, int id, int age) {
            this.name = name;
            this.id = id;
            this.age = age;
        }
    }

    public static class IdAscendingComprator implements Comparator<Student> {

        @Override
        public int compare(Student o1, Student o2) {
            return o1.id - o2.id;
            // 等价于：
            // if (o1.id < o2.id) {
            //     return -1;
            // }
            // else if (o1.id > o2.id) {
            //     return 1;
            // }
            // else {return 0;}
        }
    }

    public static class IdDescendingComparator implements Comparator<Student> {
        
        @Override
        public int compare(Student o1, Student o2) {
            return o2.id - o1.id;
        }
    }

    public static class AgeAscendingComparator implements Comparator<Student> {
        @Override
        public int compare(Student o1, Student o2) {
            return o1.age - o2.age;
        }
    }

    public static class AgeDescendingComparator implements Comparator<Student> {
        @Override
        public int compare(Student o1, Student o2) {
            return o2.age - o1.age;
        }
    }

    public static void printStudents(Student[] students) {
        for (Student student : students) {
            System.out.println("Name: " + student.name + " Id: " + student.id + " Age: "+ student.age);
        }
        System.out.println("====================================");
    }

    public static void main(String[] args) {
        Student s1 = new Student("A", 1, 23);
        Student s2 = new Student("B", 2, 21);
        Student s3 = new Student("C", 3, 22);

        Student[] students = new Student[] {s1, s2, s3};
        printStudents(students);

        Arrays.sort(students, new IdAscendingComprator());
        printStudents((students));

        Arrays.sort(students, new IdDescendingComparator());
        printStudents(students);

        Arrays.sort(students, new AgeAscendingComparator());
        printStudents(students);

        Arrays.sort(students, new AgeDescendingComparator());
        printStudents(students);
    }
}