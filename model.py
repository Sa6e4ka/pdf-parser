import requests

dir= 'b1g0voaeihj99r85mvoi' # TOdo: dir - зарезерироаное имя строеной функции, заменить
api= 'AQVNzuqpGnVZ97YTghU4nDOvG6ZRyW4AIG2mbs3f'


def squeeze(prompt):
    prompt = {
        "modelUri": f"gpt://{dir}/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 1,
            "maxTokens": "5000"
        },

    
        "messages":  [
            {
                "role" : "system",
                "text" : f'''тебе предложен тект некоторой статьи на научную тематику. 
                Твоя задача без лишних слов сделать обзор этой статьи.
                Под фразой без лишних слов значит, что строго запрещено использование 
                каких либо знаков выделения по типу **, --, и тому подобное.
                Также строго настрого запрещается добавлять дополнитльные фразу по типу:
                "вот что я могу сказать на эту тему" и т.п. 
                Твоя задача дать только обзор статьи на основе данного тебе текста, предоставленного ниже:

                [{prompt}]
                
                '''
            }
        ]
                }
      
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {api}"}
    try:
        response = requests.post(url, headers=headers, json=prompt)
        result = response.json()
        
        return result["result"]["alternatives"][0]["message"]["text"]
    except Exception as e:
        # logger.debug(f"Ошибка в запросе к GPT в функции block1_model_1: {e}")
        return f"Ошибка : {response.status_code} или {e}"