from core.graph import G
from services.user_pref_service import UserPrefService

class Interaction:
    @staticmethod
    async def interact(user_email,interaction):
        try:
            print('hola papu',interaction)
            G.add_edge(interaction.from_node,interaction.to_node)
            print('1u3so')
            UserPrefService.add_pref(id_email=user_email,node_id=interaction.to_node)
            print('payload: ',user_email)
            G.save_graph()
            print('jey')
            return {'message': 'doit'}
        except Exception as e:
            return e

