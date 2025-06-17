import java.util.*;

class Student {
    private String jmeno;
    private List<Boolean> dochazka;

    public Student(String jmeno) {
        this.jmeno = jmeno;
        this.dochazka = new ArrayList<>();
    }

    public void zaznamDochazky(boolean pritomen) {
        dochazka.add(pritomen);
    }

    public String getJmeno() {
        return jmeno;
    }

    public List<Boolean> getDochazka() {
        return dochazka;
    }
}

public class DochazkaApp {
    private static List<Student> studenti = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        while (true) {
            System.out.println("\n1. Přidat studenta");
            System.out.println("2. Zaznamenat docházku");
            System.out.println("3. Zobrazit docházku");
            System.out.println("4. Ukončit");

            System.out.print("Vyberte akci: ");
            int volba = scanner.nextInt();
            scanner.nextLine(); 

            switch (volba) {
                case 1:
                    pridatStudenta();
                    break;
                case 2:
                    zaznamenatDochazku();
                    break;
                case 3:
                    zobrazitDochazku();
                    break;
                case 4:
                    System.out.println("Ukončování programu...");
                    return;
                default:
                    System.out.println("Neplatná volba, zkuste to znovu.");
            }
        }
    }

    private static void pridatStudenta() {
        System.out.print("Zadejte jméno studenta: ");
        String jmeno = scanner.nextLine();
        studenti.add(new Student(jmeno));
        System.out.println("Student " + jmeno + " byl přidán.");
    }

    private static void zaznamenatDochazku() {
        System.out.print("Zadejte jméno studenta: ");
        String jmeno = scanner.nextLine();
        for (Student student : studenti) {
            if (student.getJmeno().equalsIgnoreCase(jmeno)) {
                System.out.print("Je student přítomen? (ano/ne): ");
                String odpoved = scanner.nextLine();
                student.zaznamDochazky(odpoved.equalsIgnoreCase("ano"));
                System.out.println("Docházka zaznamenána.");
                return;
            }
        }
        System.out.println("Student nebyl nalezen.");
    }

    private static void zobrazitDochazku() {
        for (Student student : studenti) {
            System.out.println("Student: " + student.getJmeno() + " | Docházka: " + student.getDochazka());
        }
    }
}