drop table if exists cars;

create table cars (
  _id text primary key,
  make text not null,
  year number not null,
  color text not null,
  price number not null,
  hasSunroof boolean not null,
  isFourWheelDrive boolean not null,
  hasLowMiles boolean not null,
  hasPowerWindows boolean not null,
  hasNavigation boolean not null,
  hasHeatedSeats boolean not null
);
