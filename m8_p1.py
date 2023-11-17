import re
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

intent_dict = {
    r"\batualizar|cartao|credito": "a1",
    r"\bmudar|forma|pagamento": "a2",
    r"\bmetodo|pagamento\s+ desatualizado|desatualizado": "a3",
    r"\bproceder|para\s+ atualizar": "a4",
    r"\bstatus\sdo\smeu\spedido|status": "b1",
    r"\brastrear\smeu\spedido|rastrear": "b2",
    r"\bonde\sesta\smeu\spedido": "b3",

 
}


action_dict = {
    'a1': 'Olá! Para atualizar seu cartão de crédito você deve abrir o app e clicar em "cartões".', 
    'a2': 'Olá! Para mudar a forma de pagamento, você pode só pagar em dinheiro.',
    'a3': 'Olá! Para mudar as informações de pagamento, vá em atualizar informações, contido no seu perfil.',  
    'a4': 'Olá! Se você recebeu a mensagem "Método de pagamento desatualizado", por favor, faça o L.',
    'b1': 'Olá!b1',
    'b2': 'Olá!b2',
    'b3': 'Olá!b3'

    

}

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(
            msg_type=Twist,
            topic='turtle1/cmd_vel',
            qos_profile=10
        )
        self.commands = []  

    def chatbot(self):
        command = input("Enter your command: ")
        self.process_command(command)

    def process_command(self, command):
        for chave, intencao in intent_dict.items():
            pattern = re.compile(chave)
            captura = pattern.findall(command)
            if captura:
                ponto = action_dict[intencao]
                self.commands.append(ponto)
                break  

    def execute_commands(self):
        for ponto in self.commands:
            print = ponto
            self.get_logger().info('Resposta do servidor={}'.format(print))

    def main(self):
        more_commands = "y"
        while more_commands.lower() == "y":
            self.chatbot()
            more_commands = input("Do you have more commands? (y/n): ")

        self.execute_commands()

def main(args=None):
    rclpy.init(args=args)
    tc = TurtleController()
    tc.main()
    tc.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
