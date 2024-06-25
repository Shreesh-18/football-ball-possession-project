import sys
sys.path.append('../')
from utils import get_center_bbox,measure_distance

class PlayerBallAssigner():
    def __init__(self):
        self.max_player_ball_distance=65

    def assign_ball_to_player(self,players,ball_bbox):
        ball_position=get_center_bbox(ball_bbox)

        min_dis=999999
        assigned_player=-1

        for player_id,player in players.items():
            player_bbox = player['bbox']

            dist_left=measure_distance((player_bbox[0],player_bbox[-1]),ball_position)
            dist_right=measure_distance((player_bbox[2],player_bbox[-1]),ball_position)
            dist=min(dist_left,dist_right)

            if dist < self.max_player_ball_distance:
                min_dis=dist
                assigned_player=player_id

        return assigned_player        


    

