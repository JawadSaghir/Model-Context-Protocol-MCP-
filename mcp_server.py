from mcp.server.fastmcp import FastMCP
from pydantic import Field
from typing import Any

mcp= FastMCP(
      name= "MCP Server",
      stateless_http= True,
      instructions= "You are an Mcp Server"
        )
docs={
      "doc_1.txt": "D:\\mcp_openai-agent-sdk\\doc_1.txt",
      "doc_2.txt": "D:\\mcp_openai-agent-sdk\\doc_2.txt"  
}

@mcp.tool(
        name= "read_doc_contents",
        description= "Read the contents of the document and return it as a string."
        )
def read_docs(
      doc_url: str= Field(description= "Document path")
      ) -> str:
        
        """
        This function will read the docs and return it in the form of  string

        Args:
            doc_url: "This Argument gets the file path"

        """
        try:
            with open(doc_url, "r", encoding="utf-8") as f:
                text = f.read()
                return str(text)
        except FileNotFoundError:
              print("Sorry, The file is not found")

@mcp.tool(
            name= "Update_docs_content",
            description= "This will update the contents in the file by adding new data." 
         )
def update_docs(
      doc_url: str= Field(description= "get the doc location"),
      new_data: str | None= Field(description= "get the new data to be placed in the file.")
      ) ->str :
    
    """
    The function updates the docs provided with the new string

    Args:
        doc_url: "gets the file location"
        new_data: "Data that is needed to be added in the file"

    """
    try:
        with open(doc_url, "r+") as f:
                f.write(new_data)
                updated_docs = f.read()
                return  str(updated_docs)
    except FileNotFoundError:
             return "Sorry, The file is not found"

@mcp.resource(
            uri= "docs://documents",
            name= "Resources list", 
            description= "Return the document in the string form",
            mime_type= "application/json"
            )
      
def list_docs() ->list[str]:
      """
      Returns the ist of resources
      """
      return list(docs.keys())

@mcp.resource(
      uri= "docs://documents/{doc_id}",
      mime_type= "text/plain",
      name= "fetch Specific Document",
      description= "Return the data of the specific document."
) 

def fetch_doc(doc_id: str= Field(description= "Receive doc_id")) ->str:
        """
        This will fetch the doc content for the user

        Args:
            doc_id: "Doc id of the document"
        """
        if  doc_id in docs:
            with open(docs[doc_id], "r+") as file:
                text= file.read()
                return str(text)
        else:
            raise FileNotFoundError("Sorry, The file is not found with provided id" )
              
      
mcp_app= mcp.streamable_http_app()

