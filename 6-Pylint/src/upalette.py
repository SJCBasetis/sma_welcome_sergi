"""
    Module to use colors in Python
"""

# The name starts with "_" because it is an internal constant
_colors = {
    "red":          {50:"#FFEBEE", 100:"#FFCDD2", 200:"#EF9A9A", 300:"#E57373", 400:"#EF5350"},
    "pink":         {50:"#FCE4EC", 100:"#F8BBD0", 200:"#F48FB1",300:"#F06292", 400:"#EC407A"},
    "purple":       {50:"#F3E5F5", 100:"#E1BEE7", 200:"#CE93D8", 300:"#BA68C8", 400:"#AB47BC"},
    "deep purple":  {50:"#EDE7F6", 100:"#D1C4E9", 200:"#B39DDB", 300:"#9575CD", 400:"#7E57C2"},
    "indigo":       {50:"#E8EAF6", 100:"#C5CAE9", 200:"#9FA8DA", 300:"#7986CB", 400:"#5C6BC0"},
    "blue":         {50:"#E3F2FD", 100:"#BBDEFB", 200:"#90CAF9", 300:"#64B5F6", 400:"#42A5F5"},
    "light blue":   {50:"#E1F5FE", 100:"#B3E5FC", 200:"#81D4FA", 300:"#4FC3F7", 400:"#29B6F6"},
    "cyan":         {50:"#E0F7FA", 100:"#B2EBF2", 200:"#80DEEA", 300:"#4DD0E1", 400:"#26C6DA"},
    "teal":         {50:"#E0F2F1", 100:"#B2DFDB", 200:"#80CBC4", 300:"#4DB6AC", 400:"#26A69A"},
    "green":        {50:"#E8F5E9", 100:"#C8E6C9", 200:"#A5D6A7", 300:"#81C784", 400:"#66BB6A"},
    "light green":  {50:"#F1F8E9", 100:"#DCEDC8", 200:"#C5E1A5", 300:"#AED581", 400:"#9CCC65"},
    "lime":         {50:"#F9FBE7", 100:"#F0F4C3", 200:"#E6EE9C", 300:"#DCE775", 400:"#D4E157"},
    "yellow":       {50:"#FFFDE7", 100:"#FFF9C4", 200:"#FFF59D", 300:"#FFF176", 400:"#FFEE58"},
    "amber":        {50:"#FFF8E1", 100:"#FFECB3", 200:"#FFE082", 300:"#FFD54F", 400:"#FFCA28"},
    "orange":       {50:"#FFF3E0", 100:"#FFE0B2", 200:"#FFCC80", 300:"#FFB74D", 400:"#FFA726"},
    "deep orange":  {50:"#FBE9E7", 100:"#FFCCBC", 200:"#FFAB91", 300:"#FF8A65", 400:"#FF7043"},
    "brown":        {50:"#EFEBE9", 100:"#D7CCC8", 200:"#BCAAA4", 300:"#A1887F", 400:"#8D6E63"},
    "grey":         {50:"#FAFAFA", 100:"#F5F5F5", 200:"#EEEEEE", 300:"#E0E0E0", 400:"#BDBDBD"},
    "blue grey":    {50:"#ECEFF1", 100:"#CFD8DC", 200:"#B0BEC5", 300:"#90A4AE", 400:"#78909C"},
    "black":        {50:"#000000", 100:"#000000", 200:"#000000", 300:"#000000", 400:"#000000"},
    "white":        {50:"#FFFFFF", 100:"#FFFFFF", 200:"#FFFFFF", 300:"#FFFFFF", 400:"#FFFFFF"}
}

def get_colors(clist):
    """
        Obtain the color code in Hex with the name of the color and a number
        Args:
            clist: Tuple or list of tuples composed of color name and number
        Returns:
            String or list of string with the hexa code of the colors asked
    """
    if isinstance(clist,list):
        output = [_colors[color.lower()][index] for color, index in clist]

    else:
        return _colors[clist[0]][clist[1]]

    #If there is only 1 color it shouldn't return a list
    return output if len(clist) > 1 else output[0]
