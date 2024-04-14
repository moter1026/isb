package java_prog;
import java.util.Random;
import java.util.Date;
import java.io.FileWriter;
import java.io.IOException;
import java_prog.consts.Consts;

public class PseudoRandomNumberGenerator {
    public static void main(String[] args) {        
        // Создаем объект Date, представляющий текущее время
        Date currentDate = new Date();

        // Получаем текущее время в миллисекундах
        long seed = currentDate.getTime();

        Random random = new Random(seed);
        
        try {
            FileWriter writer = new FileWriter(Consts.FILE_PATH);
            
            for (int i = 0; i < Consts.SUBSEQUENCE_LEN; i++) {
                int randomNumber = random.nextInt(2); // Генерируем случайное целое число от 0 до 2
                String number = Integer.toString(randomNumber % 2);
                writer.write(number);
            }

            // Закрываем файл после записи
            writer.close();
        } catch (IOException e) {
            System.err.println("Ошибка при записи данных в файл: " + e.getMessage());
        }
    }
}