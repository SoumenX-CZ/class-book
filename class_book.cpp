#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Student {
    string name;
    int attendance;
};

class AttendanceManager {
private:
    vector<Student> students;

public:
    void addStudent(const string& name) {
        students.push_back({name, 0});
    }

    void markAttendance(const string& name) {
        for (auto& student : students) {
            if (student.name == name) {
                student.attendance++;
                cout << "Docházka zaznamenána pro: " << name << endl;
                return;
            }
        }
        cout << "Student nenalezen!" << endl;
    }

    void displayAttendance() {
        cout << "\nPřehled docházky:\n";
        for (const auto& student : students) {
            cout << student.name << " - " << student.attendance << " dní\n";
        }
    }
};

int main() {
    AttendanceManager manager;
    int choice;
    string name;

    do {
        cout << "\n1. Přidat studenta\n2. Zaznamenat docházku\n3. Zobrazit docházku\n4. Konec\nVyberte možnost: ";
        cin >> choice;
        cin.ignore();

        switch (choice) {
            case 1:
                cout << "Zadejte jméno studenta: ";
                getline(cin, name);
                manager.addStudent(name);
                break;
            case 2:
                cout << "Zadejte jméno studenta: ";
                getline(cin, name);
                manager.markAttendance(name);
                break;
            case 3:
                manager.displayAttendance();
                break;
            case 4:
                cout << "Ukončuji aplikaci...\n";
                break;
            default:
                cout << "Neplatná volba, zkuste to znovu.\n";
        }
    } while (choice != 4);

    return 0;
}