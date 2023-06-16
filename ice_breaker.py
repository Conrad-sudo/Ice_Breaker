from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties import linkedin




if __name__ == "__main__":

    llm=ChatOpenAI(temperature=1, model_name="gpt-3.5-turbo")

    summary_template="given the information {information} about a person, I want you to create: " \
                     "1. a short summary" \
                     "2. two interesting facts about them"


    summary_prompt_template= PromptTemplate(input_variables=["information"], template=summary_template)

    #create a chain to run our LLM
    chain= LLMChain(llm=llm,prompt=summary_prompt_template)



    linkedin_data=linkedin.scrape_linkedin_profile(linkedin_profile_url="blah")

    print(chain.run(information=linkedin_data))

