from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int, b:int)-> int:
    """
    Add Two Numbers
    
    Args:
        a (int): 1st variable
        b (int): 2nd variable
    
    Returns
        int: Sum of variable a and b
    """
    return a + b

@mcp.tool()
def multiple(a:int, b:int)-> int:
    """Multiply two numbers
    
    Args:
        a (int): 1st variable
        b (int): 2nd variable
    
    Returns
        int: Multiple of variable a and b
    """
    return a * b


if __name__ == "__main__":
    mcp.run(transport="stdio")