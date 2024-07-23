from translator.basetranslator import basetrans


class TS(basetrans):
    def langmap(self):
        return {"zh": "chs", "cht": "cht"}

    def translate(self, text):
        converter = self.config["converterCHS"] if self.tgtlang != "cht" else self.config["converterCHT"]
        
        params = {
            "text": text,
            "converter": converter
        }
        response = self.proxysession.post(
            "https://api.zhconvert.org/convert", params=params
        )

        try:
            return response.json()["data"]["text"]
        except:
            raise Exception(response.text)
