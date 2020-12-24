import java.io.*;
import java.util.Scanner;
/**
 * Class Counter to count sum of data and how many data in the file.
 * @author Puvana Swatvanith
 */
public class Counter {

    // collect sum of data.
    public double sum;
    // count how many data.
    public int count;

    /**
     * filename method. to read and count sum and the number of values in the file.
     * @param filename
     */
    public void readfile(String filename){
        // File file = new File(filename);
        try {
            File file = new File(filename);
            Scanner myReader = new Scanner(file);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                // System.out.println(data);
                if(data.startsWith("#") || data.isBlank()){
                    continue;
                }
                else{
                    sum += Double.parseDouble(data);
                    count++;
                }
            }
            myReader.close();
        } catch (FileNotFoundException e) {
                System.out.println("File not found: "+ filename);
        }
    }

    /**
     * getCount method. to return the value of count;
     * @return
     */
    public int getCount(){
        return count;
    }

    /**
     * getTotal method. to return the value of sum.
     * @return
     */
    public double getTotal(){
        return sum;
    }
}