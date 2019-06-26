import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.Scanner;
import java.util.InputMismatchException;
import java.io.File;

public class Blink extends AudioPlayerExample1
{
    private static JFrame frame; 
    private static Scanner sc=new Scanner(System.in);
    public static int subject, trial;
    public static String rating, date;
    public static boolean practice;

    public static void main (String[] args)
    {
        S.lnprintln("--- Blink Supression Study ---");
       
            scansub();
            File file = new File("Error_"+subject+".ls");           
            if(!file.exists())
            {
                    trial=1;
                    String intro="";
                    intro += "Blink suppression task--out of scanner"+ "\n\n"+"Subject: "+subject+"  \t";
                    G.filename+= subject + "_";
                //Date
                    intro += "Date: "+Clock.prettydate() + "\n\n";
                if(subject%2==0) rating="effort"; else rating="discomfort";//determines 1st type of trials to do
                    intro += "Rating: "+rating+"\n";
                //  G.filename+= rating + "_";
                    G.filename+= Clock.datetime();
                    Write.file(G.filename,"dat",intro); G.filename+=".dat";
                }
            
            else
                BlinkPanel.getErrorDat(subject);
                                
         if (trial==1) phaseOne ();
   }
   public static void phaseOne()
    {
       
        if(frame!=null)
            frame.dispose(); 
        if ((trial==1 || trial==2) && (subject%2==0)) {rating ="effort";}
        if ((trial==1 || trial==2) && (!(subject%2==0))) {rating ="discomfort";}
        if ((trial==3 || trial==4) && (subject%2==0)) {rating ="discomfort";}
        if ((trial==3 || trial==4) && (!(subject%2==0))) {rating ="effort";}
        if (trial==4) {Write.to(G.filename,"/Rating: "+rating+"\n");}
        moveMouse();
        if (trial==1 || trial==3) {BlinkPanel.practice=true; BlinkPanel.numSessions=1; S.println("Subject will be doing a practice trial. Subject will be rating "+rating+". "
               +"\nPress enter to begin..."); 
        sc.nextLine();}
        if (trial==2 || trial==4) {BlinkPanel.practice=false; BlinkPanel.numSessions=5; S.println("Subject will be doing "
            +BlinkPanel.numSessions+" nonpractice trials. Subject will be rating "+rating+". " +"\nPress enter to begin..."); 
        sc.nextLine();}
        frame = new JFrame ("Suppression - "+rating);  
        if (BlinkPanel.practice=false) {
        frame.addWindowListener(new WindowAdapter(){
              public void windowClosing(WindowEvent e)
              { emergencyExit();}
        });
    }
        frame.setBounds(G.runScreenWidth,0,G.WIDTH,G.HEIGHT);
        frame.setDefaultCloseOperation (JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(new BlinkPanel());
        frame.pack(); 
        frame.setVisible(true);
        }
   public static void exit()
    {
        frame.dispose();
        String closemessage="Completed "+(BlinkPanel.displaytrialnum+1)
                           +" of "+(BlinkPanel.numSessions*2)
                           +" trials.";
        frame = new JFrame ("Rating over"); 
        frame.setLocation(G.WIDTH/4+1400,G.HEIGHT/4);
        frame.setDefaultCloseOperation (JFrame.EXIT_ON_CLOSE);
        frame.setPreferredSize (new Dimension(300,90));
        JLabel label = new JLabel(closemessage);
        label.setHorizontalAlignment(JLabel.CENTER);
        frame.add(label);
        frame.pack();
        frame.setVisible(true); 
        frame.dispose();
    }
    public static void emergencyExit()
    {
        S.printbr("Incomplete Session"
               +"\nApx. time exit: "+Clock.time(Clock.complete)
               +"\nTrial: "+trial
               +"\n"+BlinkPanel.gettrialnum()+" of "+BlinkPanel.numSessions
                   +" "+rating+" sessions completed.");
        
        Write.to(G.filename,"\nEarly exit\n"
               +BlinkPanel.gettrialnum()+" of "+BlinkPanel.numSessions
                   +" "+rating+" trials completed.\n\n");
        
        BlinkPanel.writeError();
    }  
    public static void scansub()//scan subject title
    {
        S.print ("Subject: ");
        try{ subject=Blink.sc.nextInt();}
        catch(InputMismatchException e){
                S.println("Invalid Input-must enter integer value");
                sc.nextLine();scansub();
            }
            if(subject<0) subject*=-1;
            sc.nextLine();}
    public static void moveMouse()
    {
        try{
            Robot robot = new Robot();
            robot.mouseMove(G.WIDTH+G.runScreenWidth/2,G.HEIGHT);
        }catch(AWTException awte) { S.println("AWTException thrown: "+awte.getMessage()); }
    }
} 