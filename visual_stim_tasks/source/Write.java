import java.io.*;

public abstract class Write
{
    public static void file(String title, String type, String text)
    {
        try{
            Writer output = null;
            File file = new File(title+"."+type);
            output = new BufferedWriter(new FileWriter(file));
            output.write(text);
            output.close();
        }
        catch(IOException ioe){System.out.println("IOException: "+ioe.getMessage());}
    }
    public static void file(String title, String text)
    {   file(title, "txt", text);   }
    public static void file(String text)
    {   file("file", "txt", text);   }
    
    public static void to(String filename, String text)
    {
        try{
            FileWriter fw = new FileWriter(filename,true); //the true will append the new data
            fw.write(text);//appends the string to the file
            fw.close();
        }
        catch(IOException ioe){System.out.println("IOException: "+ioe.getMessage());}
    }
}