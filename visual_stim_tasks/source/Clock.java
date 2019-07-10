import java.util.Date;
import java.text.DateFormat;
import java.text.SimpleDateFormat;

import java.util.GregorianCalendar;
import java.text.DecimalFormat;

public abstract class Clock
{
    public static String complete="HH:mm:ss, dd.MM.YYYY", 
                         simple="HH:mm";
    
    public static String time(String format)
    {
        DateFormat dateFormat = new SimpleDateFormat(format);
        Date date = new Date();
        return dateFormat.format(date);
    }
    
    public static String xFullTime(int precision) //x - exact
    {   // where precision is the number of decimal places in seconds
        String format = "yyyyMMddHHmmss";
        if(precision>0){
            format+=".";
            for(int n=0; n<precision && n<6; n++)//6 is greates precision
                format+="S";
        }
        DateFormat dateFormat = new SimpleDateFormat(format);
        Date date = new Date();
        return dateFormat.format(date);
    }
    public static String xtime(int precision)
    {
        String format = "HHmmss";
        if(precision>0){
            format+=".";
            for(int n=0; n<precision && n<6; n++)
                format+="S";
        }
        DateFormat dateFormat = new SimpleDateFormat(format);
        Date date = new Date();
        return dateFormat.format(date);
    }
    
    public static String time()
    {   return time(simple);/*HH:mm*/   }
    public static String precisetime()
    {
        DateFormat dateFormat = new SimpleDateFormat("HH:mm:ss.SSS");
        Date date = new Date();
        return dateFormat.format(date);
    }
    
    public static String datetime()
    {
        DateFormat dateFormat = new SimpleDateFormat("yyyyMMddHHmm");
        Date date = new Date();
        return dateFormat.format(date);
    }
    
    public static String date()
    {
        DateFormat dateFormat = new SimpleDateFormat("yyyyMMdd");
        Date date = new Date();
        return dateFormat.format(date);
    }
    public static String prettydate()
    {
        DateFormat dateFormat = new SimpleDateFormat("dd.MM.yyyy");
        Date date = new Date();
        return dateFormat.format(date);
    }
    
    
    
    public static int getYear()
    {
        DateFormat dateFormat = new SimpleDateFormat("yyyy");
        Date date = new Date();
        return toInt(dateFormat.format(date));
    }
    public static int getMonth()
    {
        DateFormat dateFormat = new SimpleDateFormat("MM");
        Date date = new Date();
        return toInt(dateFormat.format(date));
    }
    public static int getDay()
    {
        DateFormat dateFormat = new SimpleDateFormat("dd");
        Date date = new Date();
        return toInt(dateFormat.format(date));
    }
    public static int getHours()
    {
        DateFormat dateFormat = new SimpleDateFormat("HH");
        Date date = new Date();
        return toInt(dateFormat.format(date));
    }
    public static int getMinutes()
    {
        DateFormat dateFormat = new SimpleDateFormat("mm");
        Date date = new Date();
        return toInt(dateFormat.format(date));
    }
    public static int getSeconds()
    {
        DateFormat dateFormat = new SimpleDateFormat("ss");
        Date date = new Date();
        return toInt(dateFormat.format(date));
    }
    public static double getxSeconds()
    {
        DateFormat dateFormat = new SimpleDateFormat("ss.SSS");
        Date date = new Date();
        return toDouble(dateFormat.format(date));
    }
    
    public static double getFracDay()
    {
        return (((double)getHours()*60+getMinutes())*60+getxSeconds())/(24*60*60);
    }
    public static double getFracYear()
    {
        GregorianCalendar cal = new GregorianCalendar();
        return ((double)cal.get(GregorianCalendar.DAY_OF_YEAR)+getFracDay())/365.24219;
    }
    public static double getStardate()
    {
        return getYear()+getFracYear();
    }
    public static String stardate()
    {
        DecimalFormat fmt = new DecimalFormat(".000");
        return fmt.format(getStardate());
    }
    
    
    public static int toInt(String date)
    {   return Integer.parseInt(date);   }
    public static double toDouble(String date)
    {   return Double.parseDouble(date);   }
}
