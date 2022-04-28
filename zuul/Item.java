
/**
 * Assignment 4
 * Used the provided sample solution to assignment 3.
 * 
 * This class represents an item which may be put
 * in a room in the game of Zuul.
 * 
 * @author Lynn Marshall 
 * @version A3 Solution
 * 
 * @author Sami Mnif (101199669)
 * @version 2022.03.19
 */
public class Item
{
    // description of the item
    private String description;
    
    // weight of the item in kilgrams 
    private double weight;
    
    // short name to refer to item
    private String name;
    /**
     * Constructor for objects of class Item.
     * 
     * @param name The short name for the item
     * @param description The description of the item
     * @param weight The weight of the item
     */
    public Item(String name, String description, double weight)
    {
        this.name = name;
        this.description = description;
        this.weight = weight;
    }

    /**
     * Returns a description of the item, including its name,
     * description and weight.
     * 
     * @return  A description of the item (name , description and weight)
     */
    public String getDescription()
    {
        return name + ": " + description + " that weighs " + weight + "kg.";
    }
    
    /**
     * Returns the short name for the item.
     * 
     * @return name of the item in String
     */
    public String getName()
    {
        return name;
    }
}
