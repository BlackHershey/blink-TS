import java.util.ArrayList;

public abstract class S
{
    private static int yelpnum=0;
    public static void yelp()
    {   System.out.println("At " + ++yelpnum);   }//for debugging
    public static void yelp(int it)
    {   System.out.println("At " + it);   }//for specific moments
    
    
    public static void print()
    {   System.out.print("");   }
    public static void print(int it)
    {   System.out.print(it);   }
    public static void print(Object it)
    {   System.out.print(it);   }
    
    public static void ln()
    {   System.out.println();   }
    public static void println()
    {   System.out.println();   }
    public static void println(int it)
    {   System.out.println(it);   }
    public static void println(Object it)
    {   System.out.println(it);   }
    
    public static void br()
    {   System.out.println("\n");   }
    public static void printbr()
    {   System.out.println("\n");   }
    public static void printbr(int it)
    {   System.out.println(it+"\n");   }
    public static void printbr(Object it)
    {   System.out.println(it+"\n");   }
    
    public static void lnprint(int it)
    {   System.out.print("\n"+it);   }
    public static void lnprint(Object it)
    {   System.out.print("\n"+it);   }
    
    public static void lnprintln()
    {
        System.out.println("\n");
    }
    public static void lnprintln(int it)
    {
        System.out.println("\n"+it);
    }
    public static void lnprintln(Object it)
    {
        System.out.println("\n"+it);
    }
    
    public static void lnprintbr()
    {
        System.out.println("\n\n");
    }
    public static void lnprintbr(int it)
    {
        System.out.println("\n"+it+"\n");
    }
    public static void lnprintbr(Object it)
    {
        System.out.println("\n"+it+"\n");
    }
    
    public static void brprintln()
    {
        System.out.println("\n\n");
    }
    public static void brprintln(int it)
    {
        System.out.println("\n\n"+it);
    }
    public static void brprintln(Object it)
    {
        System.out.println("\n\n"+it);
    }
    
    public static void brprintbr()
    {
        System.out.println("\n\n\n");
    }
    public static void brprintbr(int it)
    {
        System.out.println("\n\n"+it+"\n");
    }
    public static void brprintbr(Object it)
    {
        System.out.println("\n\n"+it+"\n");
    }
    
    public static void brprint()
    {
        System.out.print("\n\n");
    }
    public static void brprint(int it)
    {
        System.out.print("\n\n"+it);
    }
    public static void brprint(Object it)
    {
        System.out.print("\n\n"+it);
    }
    
    
    public static void clear()
    {
        for (int n=0; n<25; n++)
            printbr();
    }
    
    
    
    
    public static String toData(int[] array) //default num cols = 2
    {
        String report="";
        for (int n=0; n<array.length; n++)
        {
            report+=array[n]; n++;
            report+="\t"+array[n]+"\n";
        }
        return report;
    }
    public static String toData(double[] array) //default num cols = 2
    {
        String report="";
        for (int n=0; n<array.length; n++)
        {
            report+=array[n]; n++;
            report+="\t"+array[n]+"\n";
        }
        return report;
    }
    public static String toData(int[] array, int numcols)
    {
        if (numcols<1) return "Error: invalid number of columns"; 
        int length = array.length;
        if (numcols>length) return "Error: insufficient data";
        while (length%numcols!=0) length--;
        String report="";
        for (int n=0; n<length; n++)
        {
            for (int m=0; m<numcols; m++)
            {
                report+=array[n+m]; 
                if (m<numcols-1) report+="\t"; 
                else report+="\n";
            }
            n+=numcols-1;
        }
        return report;
    }
    public static String toData(double[] array, int numcols)
    {
        if (numcols<1) return "Error: invalid number of columns"; 
        int length = array.length;
        if (numcols>length) return "Error: insufficient data";
        while (length%numcols!=0) length--;
        String report="";
        for (int n=0; n<length; n++)
        {
            for (int m=0; m<numcols; m++)
            {
                report+=array[n+m]; 
                if (m<numcols-1) report+="\t"; 
                else report+="\n";
            }
            n+=numcols-1;
        }
        return report;
    }
    
    
    public static String toCol(ArrayList<String> array)
    {
        String report="";
        for (int n=0; n<array.size(); n++)
            report+=array.get(n).toString()+"\n";
        return report;
    }
    
    public static String toData(Object[] array, int col)
    {
        String report="";
        for (int n=0; n<array.length; n++)
        {
            report+=array[n]; n++;
            for(int m=0; m<col; m++)
                report+="\t"+array[n++]+"\n";
        }
        return report;
    }
    public static String toData(ArrayList<Object> array, int col)
    {
        String report="";
        for (int n=0; n<array.size(); n++)
        {
            report+=array.get(n); n++;
            for(int m=0; m<col; m++)
                report+="\t"+array.get(n++)+"\n";
        }
        return report;
    }
    
    
    public static void toData(ArrayList array1, ArrayList<Integer> array2)
    {
        int length=array1.size();
        if (array2.size()<length)
            length=array2.size();
        String report="";
        
        for (int n=0; n<length; n++)
            report+=""+array1.get(n)+"\t"+array2.get(n)+"\n";
            
        print(report);
    }
    
    
    //check other printing things - arrays, araylists
}
