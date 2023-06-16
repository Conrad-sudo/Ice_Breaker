
from langchain import PromptTemplate

from langchain.chat_models import ChatOpenAI

from langchain.agents import Tool, initialize_agent,AgentType






def lookup( name:str)->str:
    llm = ChatOpenAI(temperature=0.3, model_name="gpt-3.5-turbo")

    template={

        """
        Given the full name {name_of_person}, I want you to retrieve a link to their Linkedin profile page.
        The link should only contain a url
        """
    }

    tools=[Tool(name="Crawl Google for linkedin profile page",func="",description="useful when you need to get a linkedin page url ")]

    agent= initialize_agent(llm=llm,tools=tools,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)

    prompt_template=PromptTemplate(input_variables=["name_of_person"], template=template)

    linkedin_profile_url=agent.run(prompt_template.format_prompt(name_of_person=name))


    return linkedin_profile_url