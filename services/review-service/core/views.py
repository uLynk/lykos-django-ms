from rest_framework import viewsets, permissions
from .models import Avaliacao
from .serializers import AvaliacaoSerializer

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny] # Aberto para testes iniciais

    def perform_create(self, serializer):
        # Em produção, pegaremos o ID do usuário logado:
        # user_id = self.request.user.id
        
        # Para teste, vamos fixar que o usuário 2 está avaliando
        user_id = 2 
        serializer.save(avaliador_id=user_id)