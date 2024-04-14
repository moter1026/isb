package java_prog;
import java.util.Random;
import java.util.Date;
import java.io.FileWriter;
import java.io.IOException;

public class PseudoRandomNumberGenerator {
    public static void main(String[] args) {
        int subsequenceLen = 128;
        
        // Создаем объект Date, представляющий текущее время
        Date currentDate = new Date();

        // Получаем текущее время в миллисекундах
        long seed = currentDate.getTime();

        Random random = new Random(seed);
        
        String filePath = "../out_java.txt";
        
        try {
            FileWriter writer = new FileWriter(filePath);
            
            for (int i = 0; i < subsequenceLen; i++) {
                int randomNumber = random.nextInt(100); // Генерируем случайное целое число от 0 до 99
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