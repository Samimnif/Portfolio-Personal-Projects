import java.util.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

/**
 * A class modelling a tic-tac-toe (noughts and crosses, Xs and Os) game in a 
 * GUI window.
 * 
 * @author Sami Mnif (101199669)
 * @version 2022.04.02
 */

public class TicTacToeGUI implements ActionListener
{ 
   private JLabel gameInfo;
   private JLabel stats;
   private JFrame frame;
   private JPanel buttonPanel;
   private JButton board[][];
   private final int SHORTCUT_MASK = Toolkit.getDefaultToolkit().getMenuShortcutKeyMaskEx();
// to save typing
   
   public static final String PLAYER_X = "X"; // player using "X"
   public static final String PLAYER_O = "O"; // player using "O"
   public static final String EMPTY = " ";  // empty cell
   public static final String TIE = "T"; // game ended in a tie
 
   private String player;   // current player (PLAYER_X or PLAYER_O)

   private String winner;   // winner: PLAYER_X, PLAYER_O, TIE, EMPTY = in progress
   
   private String startPlayer;
   private int numFreeSquares; // number of squares still free
   
   private int xWins = 0, oWins = 0, ties = 0;
   /** 
    * Constructs a new Tic-Tac-Toe board and sets up the basic
    * JFrame containing a JTextArea in a JScrollPane GUI.
    * Sets the font, title and the size of the window
    */
   public TicTacToeGUI()
   {
       startPlayer = PLAYER_X;
       gameInfo = new JLabel(winner, SwingConstants.CENTER);
       gameInfo.setFont(new Font(Font.MONOSPACED, Font.PLAIN, 20));
       gameInfo.setBackground(Color.white);
       gameInfo.setOpaque(true);
       JScrollPane scroll = new JScrollPane(gameInfo); // in scroll pane
       JFrame frame = new JFrame("TicTacToe"); //in frame
       
       stats = new JLabel("Statisctics:   X wins: "+xWins+"    O wins: "+oWins+"    Ties: "+ties);
       stats.setFont(new Font(Font.MONOSPACED, Font.PLAIN, 10));
       stats.setBackground(Color.white);
       stats.setOpaque(true);
       
       frame.setSize(350,450); //sets the window size to 300 by 400 px
       Container contentPane = frame.getContentPane();
       //contentPane.setSize(500, 500);
       contentPane.setLayout(new GridLayout(3, 1));
       contentPane.add(stats);
       
        JMenuBar menubar = new JMenuBar();
        frame.setJMenuBar(menubar);
        JMenu menu = new JMenu("Options");
        menubar.add(menu);
        
        JMenuItem newGame = new JMenuItem("New");
        JMenuItem quit = new JMenuItem("Quit");
        JMenuItem statsReset = new JMenuItem("Reset Statistics");
        JMenuItem playerChange = new JMenuItem("Change start player");
        
        quit.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_Q, SHORTCUT_MASK));
        newGame.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_N, SHORTCUT_MASK));
        statsReset.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_R, SHORTCUT_MASK));
        playerChange.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_C, SHORTCUT_MASK));
        
        quit.addActionListener(new ActionListener() {
        public void actionPerformed(ActionEvent e) {
            disableButtons();
            System.exit(0);
        }
        });
        newGame.addActionListener(new ActionListener() {
        public void actionPerformed(ActionEvent e) {
            clearBoard(); }
        });
        statsReset.addActionListener(new ActionListener() {
        public void actionPerformed(ActionEvent e) {
            xWins = 0;
            oWins = 0;
            ties = 0;
            stats.setText("Statisctics:   X wins: "+xWins+"    O wins: "+oWins+"    Ties: "+ties);}
        });
        playerChange.addActionListener(new ActionListener() {
        public void actionPerformed(ActionEvent e) {
            if (startPlayer == PLAYER_X)
        {
        startPlayer = PLAYER_O;
        }
        else
            startPlayer = PLAYER_X;}
        });
        
        menu.add(quit);
        menu.add(newGame);
        menu.add(statsReset);
        menu.add(playerChange);
        
        buttonPanel = new JPanel();
        buttonPanel.setLayout(new GridLayout(3, 3));
        clearBoard();
        
        contentPane.add(buttonPanel);
       
        //contentPane.add(gameInfo, BorderLayout.PAGE_END);
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.add(scroll); //adds scroll gui
        frame.setVisible(true); // make it visible
   }
    
    /** This action listener is called when the user clicks on a button. 
    */
    public void actionPerformed(ActionEvent e)
    {
        JButton button = (JButton)e.getSource();
        
        for (int i = 0; i < 3; i++) {
         for (int j = 0; j < 3; j++) {
            if (button == board[i][j])
            {
                board[i][j].setText(player);
                board[i][j].setEnabled(false);
                numFreeSquares--;
                    
                if (haveWinner(i,j)) 
                    winner = player; // must be the player who just went
                else if (numFreeSquares==0) 
                    winner = TIE; // board is full so it's a tie
                if (player==PLAYER_X) 
                    player=PLAYER_O;
                 else 
                    player=PLAYER_X;
            }
         }
       }
        // update the display
        if (winner != EMPTY) //checks if the game is finished or not
        {
            disableButtons();
            if (winner == TIE)
            {
                gameInfo.setForeground(Color.red);
                gameInfo.setText("Game Ended: It is a Tie");
                ties++;
            }
            else
            {
                gameInfo.setForeground(Color.blue);
                gameInfo.setText("Game Ended: " + winner + " wins");
                if (winner==PLAYER_X)
                {
                    xWins++;
                }
                else
                    oWins++;
            }
        }
        else
        {
            gameInfo.setForeground(Color.black);
            gameInfo.setText("Game In Progress: " + player + "'s turn");
        }
        stats.setText("Statisctics:   X wins: "+xWins+"    O wins: "+oWins+"    Ties: "+ties);
   }  
   
   /**
    * Sets everything up for a new game.  Marks all squares in the Tic Tac Toe board as empty,
    * and indicates no winner yet, 9 free squares and the current player is player X.
    */
   private void clearBoard()
   {
       board = new JButton[3][3];
       buttonPanel.removeAll();
      for (int i = 0; i < 3; i++) {
         for (int j = 0; j < 3; j++) {
            board[i][j] = new JButton();
            board[i][j].setBackground(Color.white);
            buttonPanel.add(board[i][j]);
            board[i][j].setEnabled(true);
            board[i][j].addActionListener(this);
         }
      }
      winner = EMPTY;
      numFreeSquares = 9;
      player = startPlayer;     // Player X always has the first turn.
      gameInfo.setForeground(Color.black);
      gameInfo.setText("Game In Progress: " + player + "'s turn");
   }
   
   /**
    * Returns true if filling the given square gives us a winner, and false
    * otherwise.
    *
    * @param int row of square just set
    * @param int col of square just set
    * 
    * @return true if we have a winner, false otherwise
    */
   private boolean haveWinner(int row, int col) 
   {
       // unless at least 5 squares have been filled, we don't need to go any further
       // (the earliest we can have a winner is after player X's 3rd move).

       if (numFreeSquares>4) return false;

       // Note: We don't need to check all rows, columns, and diagonals, only those
       // that contain the latest filled square.  We know that we have a winner 
       // if all 3 squares are the same, as they can't all be blank (as the latest
       // filled square is one of them).

       // check row "row"
       if ( board[row][0].getText().equals(board[row][1].getText()) &&
            board[row][0].getText().equals(board[row][2].getText()) ) return true;
       
       // check column "col"
       if ( board[0][col].getText().equals(board[1][col].getText()) &&
            board[0][col].getText().equals(board[2][col].getText()) ) return true;

       // if row=col check one diagonal
       if (row==col)
          if ( board[0][0].getText().equals(board[1][1].getText()) &&
               board[0][0].getText().equals(board[2][2].getText()) ) return true;

       // if row=2-col check other diagonal
       if (row==2-col)
          if ( board[0][2].getText().equals(board[1][1].getText()) &&
               board[0][2].getText().equals(board[2][0].getText()) ) return true;

       // no winner yet
       return false;
   }
   
   /**
    * disables all the buttons so the user cannot use them anymore
    */
   private void disableButtons()
   {
       for (int i = 0; i < 3; i++) {
         for (int j = 0; j < 3; j++) {
            board[i][j].setEnabled(false);
         }
      }
   }
}