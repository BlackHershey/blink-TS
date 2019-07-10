

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.ArrayList;
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class BlinkPanel extends JPanel
{
    private boolean test = false;
    public static boolean practice;
    private static int begtrialnum=0;
    public static int numSessions,displaytrialnum;
    private final int TimeLimit;
    private Timer timer;
    public long elapsedTime;
    public long startTime;
    public long currentTime;
    public String blinkText;
    private final int DELAY = 250; //Sampling rate = DELAY/1000
    //private boolean paused=true;
    //  Sets up the panel, including the timer for the animation.
    public BlinkPanel() 
    {
        timer = new Timer(DELAY, new TimerListener());
        TimeLimit = 900*numSessions;
        G.time=0;
        begtrialnum=0;
        addMouseListener (new Mouse());
        setFocusable(true);
        setPreferredSize (new Dimension(G.WIDTH, G.HEIGHT));
        setBackground (Color.black);
        String audioFilePath="E:/Test/Audio.wav";
        AudioPlayerExample1 player=new AudioPlayerExample1();
        if (Blink.trial==2 || Blink.trial==4) player.play(audioFilePath);
        startTime=System.currentTimeMillis();
        timer.start();  
          }
    
    public void paintComponent (Graphics page)
    {
        super.paintComponent (page);
        currentTime=System.currentTimeMillis();
        elapsedTime=(currentTime-startTime)/100;
        if ((elapsedTime>600 && elapsedTime<900)||(elapsedTime>1500 && elapsedTime<1800)||
                (elapsedTime>2400 && elapsedTime<2700)|| (elapsedTime>3300&&elapsedTime<3600)||
               (elapsedTime>4200&&elapsedTime<4500)){page.setColor(Color.green);}
           else {page.setColor(Color.red);}
        page.fillRect(G.WIDTH/2-G.HEIGHT/8, G.HEIGHT/16,
                      G.HEIGHT/4, G.HEIGHT/4);//paints box
        page.setColor(Color.black);
        //display intensity as ratio of height on screen
        int fontsize=G.HEIGHT*3/16;
        Font font = new Font("Arial",Font.PLAIN,fontsize);
        page.setFont(font); 
        page.drawString(""+(int)((double)(G.HEIGHT-G.Y-1)/G.HEIGHT*10),//0-9 number
                                          G.WIDTH/2-(int)(fontsize/3.4),//centers
                                          G.HEIGHT*5/32+fontsize/2);
        fontsize=G.HEIGHT/30;
        font = new Font("Arial",Font.PLAIN,fontsize);
        page.setFont(font); 
        page.drawString(Blink.rating, 
                G.WIDTH/2-G.HEIGHT/9,
                G.HEIGHT*19/64);
        page.setColor(Color.white);
        elapsedTime=(currentTime-startTime)/100;
        blinkText="";
        if ((elapsedTime>0 && elapsedTime<20)||(elapsedTime>900 && elapsedTime<920)||(elapsedTime>1800 && elapsedTime<1820)||(elapsedTime>2700 && elapsedTime<2720)
            ||(elapsedTime>3600 && elapsedTime<3620)){blinkText="Don't blink";} 
        if ((elapsedTime>600 && elapsedTime<620) || (elapsedTime>1500 && elapsedTime<1520) || 
               (elapsedTime>2400 && elapsedTime<2420) || (elapsedTime>3300&&elapsedTime<3320) 
               || (elapsedTime>4200&&elapsedTime<4220)){blinkText="OK to blink";} 
        page.drawString(blinkText,
                    G.WIDTH/2-(int)(fontsize*2.55),
                    G.HEIGHT*3/8);
       }
    
    private class TimerListener implements ActionListener
    {
            public void actionPerformed (ActionEvent event)
        {
            G.time+=(double)DELAY/1000;
            G.X = MouseInfo.getPointerInfo().getLocation().x;
            G.Y = MouseInfo.getPointerInfo().getLocation().y;
            double rating=(double)(G.HEIGHT-G.Y)/G.HEIGHT*10;
            if(rating<.0001) rating=0;    
            if(rating>9) rating=9;//puts highest rating at 9
            if ((Blink.trial==2) || (Blink.trial==4)) {Write.to(G.filename, Clock.precisetime()+ "\t" + elapsedTime+ "\t"
               +blinkText + "\t" + rating+ "\n");}
            currentTime=System.currentTimeMillis();
            elapsedTime=(currentTime-startTime)/100;
            repaint();
            displaytrialnum= (int) (G.time/90); 
            if (displaytrialnum>begtrialnum) {S.println("Trial number " + displaytrialnum);
                    begtrialnum=displaytrialnum;}
            if ((elapsedTime>TimeLimit) ||  (elapsedTime>TimeLimit) ){
                 timer.stop();
                 Write.to (G.filename, "Clock.precisetime after timer has stopped:  "
                    + Clock.precisetime()+ "\t" + elapsedTime+ "\t" + "G.time after timer has stopped:"+ "\t" + G.time + "." + "\n");
            if ((Blink.trial==2)|| (Blink.trial==4)) S.println("Trial number 5");
                 setVisible(false);
                 Blink.trial++; 
                 if (Blink.trial<5) Blink.phaseOne();
                 if (Blink.trial==5) Blink.exit(); 
                }                                 
            }
    }
    
    private class Mouse implements MouseListener
    {
        public void mousePressed (MouseEvent event) {}
        public void mouseClicked (MouseEvent event)  {} //paused=!paused;
        public void mouseReleased (MouseEvent event) {} 
        public void mouseExited (MouseEvent event)  {}
        public void mouseEntered (MouseEvent event) {}
       }
    public static int gettrialnum()
      {  return ((int)G.time)/(90);}
    
    public static void writeError()
    {S.println("WriteError");
        Write.file("Error_"+Blink.subject, "ls", G.filename
                                           +"\n"+numSessions
                                           +"\n"+gettrialnum()
                                           +"\n"+Blink.trial
                                           +"\n"+Blink.rating
                                           +"\nints{numSessions,sessionNum,trialNum}");
    }
    public static void getErrorDat(int subject)
    {
        //recover error data from file--try is William's creation, I don't know if it works (or how)
        try{
            File errorfile = new File("Error_"+subject+".ls");
            Scanner filescan = new Scanner(errorfile);
            G.filename=filescan.nextLine();
            numSessions=filescan.nextInt();
            Blink.trial=filescan.nextInt();filescan.nextLine();//do I need an extra nextline? 
            Blink.rating=filescan.nextLine();
            
            Write.to(G.filename,"Session Resumed\nApx time start:"+Clock.time(Clock.complete)+"\n");
            
            //errorfile.setWritable(true);
            //may need to close filewriter
            //if(errorfile.delete());//not working  -  no such file or directory error
        }catch(IOException ioe){S.println("IOException:get Errordat"+ioe.getMessage());}
    }
}

