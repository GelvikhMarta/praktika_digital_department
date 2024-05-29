import sqlite3
import q4

class DatabaseService:
    @staticmethod
    def input_values(name):
        cursor.execute("SELECT * FROM exercises WHERE name = ?", (name,))
        tabs = cursor.fetchall()
        tab = tabs[0]
        values = [0] * (len(tab))
        for i in range(len(tab)):
            if tab[i] == 1:
                values[i] = 1
            else:
                values[i] = 0
        return values

    @staticmethod
    def insert_tr(massive):
        cursor.execute(f"INSERT INTO training VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                       (massive[0], massive[1], massive[2], massive[3], massive[4], massive[5], massive[6], massive[7]))
        db.commit()

    @staticmethod
    def insert_ex(massive):
        cursor.execute(f"INSERT INTO exercises VALUES(?, ?, ?, ?, ?, ?, ?)",
                       (massive[0], massive[1], massive[2], massive[3], massive[4], massive[5], massive[6]))
        db.commit()


    @staticmethod
    def delete_tr(rowid):
        cursor.execute(f"DELETE FROM training WHERE rowid = ?", (rowid,))
        db.commit()

    @staticmethod
    def update_tr(massive, rowid):
        cursor.execute("UPDATE training SET Day = ?, Name = ?, Timer = ?, Sets = ?, Reps = ?, Weight = ?,\
         Specialization = ?,  Type = ? WHERE rowid = ?",
                       (massive[0], massive[1], massive[2], massive[3], massive[4], massive[5], massive[6], massive[7], rowid))
        db.commit()

    @staticmethod
    def find_train(Day):  # Для календаря
        cursor.execute("SELECT * FROM training WHERE Day = ?", (Day,))
        val = cursor.fetchone()
        print(val)
        if val != None:
            return 1
        else:
            return 0

    @staticmethod
    def print_boolean_ex(l,name):  # вывод данных для упражнения в плане тренировок
        cursor.execute("SELECT Timer,Sets,Reps,Weight FROM exercises WHERE name = ?", (name,))
        val = cursor.fetchall()
        return val[0][l]

    @staticmethod
    def print_tr(name_day):
        dbservice = DatabaseService()
        calc = Calculation()
        arr = []
        strochka = ''
        arr1 = ['Дата: ', '', 'Время: ', 'Подходы: ', 'Повторения: ', "Вес: ", "Тип мышц: "]
        print('План:')
        for i in calc.list_rowid_tr(name_day):
            arr = arr + dbservice.print_value_tr(f'{i}')
        for i in range(len(arr)):
            for j in range(7):
                if j != 0:
                    if arr[i][j] != 0:
                        strochka = strochka + f'{arr1[j]}' + f'{arr[i][j]}' + '\n' + ' '
            strochka = strochka + '. '
        arr1 = strochka.split('. ')
        return arr1

    @staticmethod
    def print_value_tr(rowid):  # вывод данных для упражнения в плане тренировок
        cursor.execute("SELECT *,rowid FROM training WHERE rowid = ?", (rowid,))
        val = cursor.fetchall()
        return val
        

    @staticmethod
    def print_alltr():  # используется для вывода ВСЕХ упражнений в плане тренировок
        cursor.execute("SELECT COUNT(*) FROM training")
        cnt = cursor.fetchone()[0]
        cursor.execute("SELECT rowid,* FROM training")
        items = cursor.fetchall()
        print(items)

    @staticmethod
    def get_names():
        cursor.execute("SELECT name FROM exercises")
        names = cursor.fetchall()
        arr = []
        for i in range(len(names)):
            arr.append(names[i][0])
        f = tuple(arr)
        return f

    @staticmethod
    def get_count():  # используется для вывода ВСЕХ упражнений в плане тренировок
        cursor.execute("SELECT COUNT(*) FROM exercises")
        cnt = cursor.fetchone()[0]
        cnt = int(cnt)
        return cnt

    @staticmethod
    def proverka(arr,name):
        cursor.execute("""SELECT * FROM exercises WHERE name = ?""", (name,))
        a = cursor.fetchone()
        massive = [0] * 8
        rowik = arr[5]
        massive[0] = arr[4]
        massive[1] = a[0]
        if a[1] != 0:
            massive[2] = arr[0]
        if a[2] != 0:
            massive[3] = arr[1]
        if a[3] != 0:
            massive[4] = arr[2]
        if a[4] != 0:
            massive[5] = arr[3]
        massive[6] = a[5]
        massive[7] = a[6]
        if arr[5] != 0:
            DatabaseService.update_tr(massive,rowik)
        else:
            DatabaseService.insert_tr(massive)
    
    @staticmethod
    def find_muscles():
        cursor.execute("SELECT Specialization from exercises")
        names = cursor.fetchall()
        arr = []
        for i in range(len(names)):
            arr.append(names[i][0])
        f = tuple(arr)
        fafa = set(f)
        return fafa
    
    @staticmethod
    def find_ex_spec(arr):
        if arr[1] != 0 or arr[2] != 0 or arr[3] != 0 or arr[4] != 0:
            if arr[1] == 0:
                cursor.execute("""SELECT name FROM exercises WHERE Specialization = ? AND (sets = ? OR reps = ? OR weight = ?)""", (arr[0],arr[2],arr[3],arr[4]))
                sunboy = cursor.fetchall()
            else:
                cursor.execute("""SELECT name FROM exercises WHERE Specialization = ? AND Timer = ?""",(arr[0],arr[1],))
                sunboy = cursor.fetchall()
        else:
            cursor.execute("""SELECT name FROM exercises WHERE Specialization = ?""", (arr[0],))
            sunboy = cursor.fetchall()
        return sunboy


class Calculation:
    @staticmethod
    def get_nameday(num_day):
        week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        day = week[num_day - 1]
        return day

    @staticmethod
    def list_rowid_tr(name_day):  # получение списка rowid для определенного дня
        cursor.execute("SELECT COUNT(*) FROM training WHERE Day = ?", (name_day,))
        cnt = cursor.fetchone()[0]
        cursor.execute("SELECT rowid FROM training WHERE Day = ?", (name_day,))
        items = cursor.fetchall()
        l_rowid = [0] * cnt
        i = 0
        for el in items:
            l_rowid[i] = el[0]
            i += 1
        return l_rowid
    @staticmethod
    def baba_print(baba):
        sunboy = baba
        return sunboy
     
    @staticmethod    
    def list_rowid_ex(): #rowid
        cursor.execute("SELECT COUNT(*) FROM exercises")
        cnt = cursor.fetchone()[0]
        cursor.execute("SELECT rowid FROM exercises")
        items = cursor.fetchall()
        l_rowid = [0]*cnt
        i = 0
        for el in items:
            l_rowid[i] = el[0]
            i += 1
        return l_rowid


def get_ex(rowid):
    cursor.execute("SELECT name FROM exercises WHERE rowid = ?", (rowid,))
    return cursor.fetchone()[0]


def print_allexercises():
    cursor.execute("SELECT rowid, name FROM exercises")
    print(cursor.fetchall())


def close_db():
    db.close()



def main():
    aboba = DatabaseService()
    dbservice = DatabaseService()
    print_allexercises()
    dbservice.print_alltr()
    close_db()


db = sqlite3.connect('database.db')
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS training (
              Day TEXT,
              Name TEXT,
              Timer INTEGER,
              Sets INTEGER,
              Reps INTEGER,
              Weight INTEGER,
              Specialization TEXT,
              Type TEXT         
    )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS exercises (
              Name TEXT,
              Timer INTEGER,
              Sets INTEGER,
              Reps INTEGER,
              Weight INTEGER,
              Specialization TEXT,
              Type TEXT
    )""")

cursor.execute("SELECT COUNT(*) FROM exercises")
cnt = cursor.fetchone()[0]
db.commit()


if __name__ == '__main__':
    arr = [0] * 7
    arr[0] = 'zaza'
    arr[1] = 1
    arr[2] = 1
    arr[3] = 0
    arr[4] = 0
    arr[5] = 'ya'
    arr[6] = 'Серёга пират'
    find_muscles()
